import os
from django.contrib.auth.views import redirect_to_login
from chat.models import *
from django.db.models.query_utils import Q
from notification.models import *
from user.models import *
from post.models import *
from post.forms import *
from group.models import *
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from pydub.silence import split_on_silence
from pydub import AudioSegment
import numpy as np
import librosa
import math
import pickle

def home(request):
    me = None if request.user.id is None else User.objects.get(id=request.user.id)
    if me is None:
        return redirect(reverse('user:login'))
    
    personnal_chats = ChatBox.objects.filter(Q(user1=me)|Q(user2=me))
    group_chats = list(GroupChatBox.objects.filter(creator=me)) + [join.groupchatbox for join in JoinGroupChat.objects.filter(invitee=me)]

    my_groups = set(list(Group.objects.filter(admins__in=[me])) + list(Group.objects.filter(members__in=[me])))

    #online_users = User.objects.filter(is_online=True)
    online_users = User.objects.filter(Q(is_online=True)&~Q(id=me.id))

    posts = Post.objects.all()

    context = {
        'posts': [{
            'view': 'list',
            'post': post,
            'reactions': Reaction.objects.filter(post=post),
            'comments': Comment.objects.filter(post=post),
        } for post in reversed(posts)],
        'me': me,
        'personnal_chats': [{
            'chat': chat,
            'receiver_id': chat.user2.id if chat.user1 == me else chat.user1.id,
        } for chat in personnal_chats],
        'group_chats': [{
            'chat': chat,
            'latest_msg': GroupMessage.objects.filter(chatbox=chat).order_by('-sent')[0]
        } for chat in group_chats],
        'my_groups': my_groups,
        'online_users': online_users,
        'my_notifications': list(reversed(PostNotification.objects.filter(recipient=me).exclude(actor=me))),
    }
    return render(request, 'home.html', context)


def get_mfcc(file_path):
    y, sr = librosa.load(file_path) # read .wav file
    hop_length = math.floor(sr*0.010) # 10ms hop
    win_length = math.floor(sr*0.025) # 25ms frame
    # mfcc is 12 x T matrix
    mfcc = librosa.feature.mfcc(
        y, sr, n_mfcc=12, n_fft=1024,
        hop_length=hop_length, win_length=win_length)
    # substract mean from mfcc --> normalize mfcc
    mfcc = mfcc - np.mean(mfcc, axis=1).reshape((-1,1)) 
    # delta feature 1st order and 2nd order
    delta1 = librosa.feature.delta(mfcc, order=1)
    delta2 = librosa.feature.delta(mfcc, order=2)
    # X is 36 x T
    X = np.concatenate([mfcc, delta1, delta2], axis=0) # O^r
    # return T x 36 (transpose of X)
    return X.T # hmmlearn use T x N matrix

def detect_leading_silence(sound, silence_threshold=-42.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms

def search(request, filename):
    me = None if request.user.id is None else User.objects.get(id=request.user.id)
    my_groups = set(list(Group.objects.filter(admins__in=[me])) + list(Group.objects.filter(members__in=[me])))

    # Get file audio
    abs_path = "E:/Code/Python/Django/tomo/tomo/voice_search_data/"
    audio_data = AudioSegment.from_file(abs_path+filename, format="wav")
    os.remove(abs_path+filename)

    # split audio into single word's audio
    audio_chunks = split_on_silence(audio_data, min_silence_len=500, silence_thresh=-30)
    # export to folder
    for i, chunk in enumerate(audio_chunks):
        out_file = "tomo/voice_search_data/chunk{0}.wav".format(i)
        print("exporting", out_file)
        chunk.export(out_file, format="wav")


    predict_words = []

    # Predict each segmented audio
    i = 0
    for audio_name in os.listdir('tomo/voice_search_data'):
        if audio_name == 'search.wav':
            continue # ignore if this is the original file
        audio_data = AudioSegment.from_file(abs_path+audio_name, format="wav")

        # trim silence
        start_trim = detect_leading_silence(audio_data)
        end_trim = detect_leading_silence(audio_data.reverse())

        trimmed_sound = audio_data[start_trim:len(audio_data)-end_trim]    
        trimmed_sound.export(f"tomo/voice_search_data/trimmed{i}.wav", format="wav")

        # get model
        class_names = ['con', 'học', 'nhà', 'sinh', 'tuyển', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'có', 'không', 'ngày', 'tháng', 'lớp']
        model = {}
        for key in class_names:
            name = f"tomo/models/model_{key}.model"
            with open(name, 'rb') as file:
                model[key] = pickle.load(file)

        # predict
        record_mfcc = get_mfcc(f"tomo/voice_search_data/trimmed{i}.wav")
        scores = [model[cname].score(record_mfcc) for cname in class_names]
        predict_word = class_names[np.argmax(scores)]

        # convert word of num into num (if exist)
        '''num = {
            'một': 1,
            'hai': 2,
            'ba': 3,
            'bốn': 4,
            'năm': 5,
            'sáu': 6,
            'bảy': 7,
            'tám': 8,
            'chín': 9,
        }
        if predict_word in num:
            predict_word = num[predict_word]'''

        predict_words.append(predict_word)
        os.remove("tomo/voice_search_data/" + audio_name)
        os.remove(f"tomo/voice_search_data/trimmed{i}.wav")
        i += 1

    # Get posts relating to predicted word
    posts_search_result = []
    all_posts = Post.objects.all()
    for post in all_posts:
        if any(str(predict_word) in post.text for predict_word in predict_words):
            posts_search_result.append(post)

    context = {
        'posts': [{
            'view': 'list',
            'post': post,
            'reactions': Reaction.objects.filter(post=post),
            'comments': Comment.objects.filter(post=post),
        } for post in reversed(posts_search_result)],
        'my_groups': my_groups,
        'predict_words': predict_words,
        'me': me,
    }
    return render(request, 'search_result.html', context)

def conv_to_num(word):
    return {
        'một': 1,
        'hai': 2,
        'ba': 3,
        'bốn': 4,
        'năm': 5,
        'sáu': 6,
        'bảy': 7,
        'tám': 8,
        'chín': 9,
    }[word]
