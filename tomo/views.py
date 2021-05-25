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

def home(request):
    me = None if request.user.id is None else User.objects.get(id=request.user.id)
    if me is None:
        return redirect(reverse('user:login'))
    
    personnal_chats = ChatBox.objects.filter(Q(user1=me)|Q(user2=me))
    group_chats = list(GroupChatBox.objects.filter(creator=me)) + [join.groupchatbox for join in JoinGroupChat.objects.filter(invitee=me)]

    my_groups = set(list(Group.objects.filter(admins__in=[me])) + list(Group.objects.filter(members__in=[me])))

    #online_users = User.objects.filter(is_online=True)
    #online_users = User.objects.filter(Q(is_online=True)&~Q(id=me.id))

    posts = Post.objects.all()
    '''posts_each_load = 1
    paginator = Paginator(posts, posts_each_load)
    page = request.POST.get('page')
    print('page' + str(page))
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)'''

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
        #'online_users': online_users,
        'my_notifications': list(reversed(PostNotification.objects.filter(recipient=me).exclude(actor=me))),
    }
    return render(request, 'home.html', context)
