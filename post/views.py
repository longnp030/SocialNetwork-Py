import pickle
import re
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from underthesea import word_tokenize
from group.models import *
from post.forms import *
from user.models import *
from post.models import *
from notification.models import *
from django.shortcuts import redirect, render
from django.urls import reverse

from chat.views import get_available_chats as gac
# Create your views here.

def create_post(request, group_id=None):
    me = None if request.user.id is None else User.objects.get(id=request.user.id)
    if request.method == 'POST':
        post_create_form = PostCreationForm(request.POST, request.FILES)
        if post_create_form.is_valid():
            post = post_create_form.save(commit=False)
            post.author = me
            post.save()
            if group_id:
                group = Group.objects.get(id=group_id)
                post.group = group
                post.save()
                GroupPost.objects.create(group=group, post=post)
            return redirect(reverse('post:add_img', kwargs={'post_id': post.id}))
    else:
        post_create_form = PostCreationForm()
    context = {
        'me': me,
        'form': post_create_form,
        'personnal_chats': gac(request)['personnal_chats'],
        'group_chats': gac(request)['group_chats'],
    }
    return render(request, 'post/create.html', context)

def detech_faces(img):
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('face_recognition/models/face_model.yml')

    img = cv2.imread(img.image.url[1:], cv2.IMREAD_GRAYSCALE)
    faces = detector.detectMultiScale(img, 1.3, 5)
    fr_ids = []
    for (x, y, w, h) in faces:
        id, dist = recognizer.predict(img[y:y+h, x:x+w])
        fr_ids.append(id)
    
    return fr_ids

def remove_html(text):
    return re.sub(r'<[^>]*>', '', text)

def remove_punct(text):
    return re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]', ' ', text)

def remove_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

def remove_stopwords(text):
    stopwords = []
    with open('topic/data/stopwords.txt', 'r', encoding='utf-8') as f:
        for stopword in f.readlines():
            stopwords.append(stopword.strip())

    return ' '.join([word for word in text.split() if word not in stopwords])

def lower(text):
    return text.lower()

def standardize(text):
    text = remove_html(text)
    text = word_tokenize(text, format='text')
    text = lower(text)
    text = remove_punct(text)
    text = remove_spaces(text)
    text = remove_stopwords(text)
    return text

def load_topic_model():
    return pickle.load(open("topic/models/linear_classifier.pkl", 'rb'))

def add_img(request, post_id):
    me = None if request.user.id is None else User.objects.get(id=request.user.id)
    post = Post.objects.get(id=post_id)
    this_post_imgs = Image.objects.filter(author=me).order_by('uploaded')

    if request.method == 'POST':
        upload_img_form = ImageUploadForm(request.POST, request.FILES)
        if upload_img_form.is_valid():
            img = upload_img_form.save(commit=False)
            img.author = me
            img.save()
            return redirect(reverse('post:add_img', kwargs={'post_id': post_id}))
    else:
        upload_img_form = ImageUploadForm()

    if request.method == 'POST':
        add_img_form = PostAddImageForm(request.POST, request.FILES, instance=post)
        if add_img_form.is_valid():
            if post.text == '' and len(add_img_form.cleaned_data['images']) == 0:
                Post.objects.get(id=post.id).delete()
                return redirect('home')
            else:
                topic_model = load_topic_model()
                label_encoder = LabelEncoder()
                label_encoder.classes_ = np.load('topic/models/label_classes.npy')
                post.topic = label_encoder.inverse_transform(topic_model.predict([post.text]))[0]
                
                if len(add_img_form.cleaned_data['images']) > 0:
                    fr_ids = []
                    for img in add_img_form.cleaned_data['images']:
                        fr_ids = fr_ids + detech_faces(img)
                    if len(fr_ids) > 0:
                        for fr_id in fr_ids:
                            post.tagged_friends.add(User.objects.get(id=fr_id))
                add_img_form.save()
                return redirect('home')
    else:
        add_img_form = PostAddImageForm(instance=post, initial={'images': this_post_imgs})

    
    context = {
        'add_img_form': add_img_form,
        'upload_form': upload_img_form,
        'tag_fr_form': None,
        'personnal_chats': gac(request)['personnal_chats'],
        'group_chats': gac(request)['group_chats'],
        'this_post_imgs': this_post_imgs,
    }
    return render(request, 'post/add_img.html', context)

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        edit_post_form = PostEditForm(request.POST, instance=post)
        if edit_post_form.is_valid():
            edit_post_form.save()
            return redirect(reverse('post:post_view', kwargs={'post_id': post_id}))
    else:
        edit_post_form = PostEditForm(instance=post)
    context = {
        'form': edit_post_form,
        'personnal_chats': gac(request)['personnal_chats'],
        'group_chats': gac(request)['group_chats'],
    }
    return render(request, 'post/edit.html', context)

def like_post(request, post_id):
    if len(Reaction.objects.filter(post=Post.objects.get(id=post_id), liker=User.objects.get(id=request.user.id))) > 0:
        return redirect(reverse('post:post_view', kwargs={'post_id': post_id}))
    Reaction.objects.create(
        post=Post.objects.get(id=post_id),
        liker=User.objects.get(id=request.user.id)
    )
    return redirect(reverse('post:post_view', kwargs={'post_id': post_id}))

def unlike_post(request, post_id):
    try:
        Reaction.objects.get(
            post=Post.objects.get(id=post_id),
            liker=User.objects.get(id=request.user.id)
        ).delete()
        PostNotification.objects.get(
            post=Post.objects.get(id=post_id),
            actor=User.objects.get(id=request.user.id),
            action='liked'
        ).delete()
    except Exception as e:
        return redirect(reverse('post:post_view', kwargs={'post_id': post_id}))
    else:
        return redirect(reverse('post:post_view', kwargs={'post_id': post_id}))

def post_view(request, post_id):
    me = User.objects.filter(id=request.user.id).first()
    post = Post.objects.get(id=post_id)
    reactions = Reaction.objects.filter(post=post)
    liked = len(reactions.filter(liker=me)) > 0
    comments = Comment.objects.filter(post=post)

    context = {
        'post_id': post_id,
        'me': me,
        'post': post,
        'liked': liked,
        'reactions': reactions,
        'comments': reversed(comments),
        'view': 'post',
        'personnal_chats': gac(request)['personnal_chats'],
        'group_chats': gac(request)['group_chats'],
        'my_notifications': list(reversed(PostNotification.objects.filter(recipient=me).exclude(actor=me))),
    }
    return render(request, 'post/post_view.html', context)

def delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('home')
