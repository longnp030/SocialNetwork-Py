from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import datetime as dt

from user.models import *
from post.models import *
from .forms import *
from chat.views import get_available_chats as gac

# Create your views here.

def create(request):
    me = None if request.user.id is None else User.objects.get(id=request.user.id)
    if request.method == 'POST':
        group_create_form = GroupCreationForm(request.POST, request.FILES)
        if group_create_form.is_valid():
            group = group_create_form.save(commit=False)
            group.creator = me
            group.save()
            group.admins.add(me)
            group.members.add(me)
            return redirect(reverse('group:view', kwargs={'group_id': group.id}))
    else:
        group_create_form = GroupCreationForm()
    context = {
        'me': me,
        'form': group_create_form,
        'personnal_chats': gac(request)['personnal_chats'],
        'group_chats': gac(request)['group_chats'],
    }
    return render(request, 'group/create.html', context)

def view(request, group_id):
    me = User.objects.get(id=request.user.id)
    group = Group.objects.get(id=group_id)

    if request.method == 'POST':
        edit_group_form = GroupEditForm(request.POST, request.FILES, instance=group)
        if edit_group_form.is_valid():
            edit_group_form.save()
            return redirect(reverse('group:view', kwargs={'group_id': group_id}))
    else:
        edit_group_form = GroupEditForm(instance=group)

    if request.method == 'POST':
        invite_member_form = GroupInvitationForm(request.POST, initial={'group': group, 'inviter': me})
        if invite_member_form.is_valid():
            invite_member_form.save()
            return redirect(reverse('group:view', kwargs={'group_id': group_id}))
    else:
        invite_member_form = GroupInvitationForm(initial={'group': group, 'inviter': me})

    context = {
        'me': me,
        'group': group,
        'edit_group_form': edit_group_form,
        'invite_member_form': invite_member_form,
        'posts': [{
            'view': 'list',
            'post': post,
            'reactions': Reaction.objects.filter(post=post),
            'liked': len(Reaction.objects.filter(post=post, liker=me)) > 0,
            'comments': Comment.objects.filter(post=post),
        } for post in reversed(group.posts.all())],
        'is_admin': Group.objects.get(id=group_id).admins.filter(id=me.id).exists(),
        'pending_join_requests': JoinGroupRequest.objects.filter(group=group),
        'all_images': PostImage.objects.filter(post__in=Post.objects.filter(group=group))[:9],
        'personnal_chats': gac(request)['personnal_chats'],
        'group_chats': gac(request)['group_chats'],
    }
    return render(request, 'group/view.html', context)

@login_required
def explore(request):
    me = None if request.user.id is None else User.objects.get(id=request.user.id)
    join_group_invitations = GroupJoinInvitation.objects.filter(invitee=me)
    joined_groups = Group.objects.filter(members__id=me.id)
    suggested_groups = [{
        'group': group,
        'join_request_sent': len(JoinGroupRequest.objects.filter(sender=me, group=group)) > 0,
    } for group in Group.objects.all().exclude(id__in=[group.id for group in joined_groups])]
    context = {
        'me': me,
        'join_group_invitations': join_group_invitations,
        'joined_groups': joined_groups,
        'suggested_groups': suggested_groups,
        'personnal_chats': gac(request)['personnal_chats'],
        'group_chats': gac(request)['group_chats'],
    }
    return render(request, 'group/explore.html', context)

def send_join_group_request(request, group_id):
    me = User.objects.get(id=request.user.id)
    group = Group.objects.get(id=group_id)
    join_group_request = JoinGroupRequest(
        group=group,
        sender=me,
        sent=dt.datetime.now,
    )
    join_group_request.save()
    return redirect(reverse('group:explore'))

def cancel_join_group_request(request, group_id):
    me = User.objects.get(id=request.user.id)
    group = Group.objects.get(id=group_id)
    join_group_request = None
    try:
        join_group_request = JoinGroupRequest.objects.get(group=group, sender=me)
    except:
        return redirect(reverse('group:explore'))
    else:
        join_group_request.delete()
    return redirect(reverse('group:explore'))

def accept_join_group_request(request, user_id, group_id):
    group = Group.objects.get(id=group_id)
    sender = User.objects.get(id=user_id)
    try:
        JoinGroupRequest.objects.get(group=group, sender=sender).delete()
    except:
        return redirect(reverse('group:view', kwargs={'group_id': group_id}))
    else:
        group.members.add(sender)
    return redirect(reverse('group:view', kwargs={'group_id': group_id}))

def reject_join_group_request(request, user_id, group_id):
    group = Group.objects.get(id=group_id)
    sender = User.objects.get(id=user_id)
    try:
        JoinGroupRequest.objects.get(group=group, sender=sender).delete()
    except:
        return redirect(reverse('group:view', kwargs={'group_id': group_id}))
    return redirect(reverse('group:view', kwargs={'group_id': group_id}))

def remove_group_member(request, user_id, group_id):
    group = Group.objects.get(id=group_id)
    member = User.objects.get(id=user_id)
    try:
        group.members.remove(member)
    except:
        return redirect(reverse('group:view', kwargs={'group_id': group_id}))

def leave_group(request, group_id):
    me = User.objects.get(id=request.user.id)
    group = Group.objects.get(id=group_id)
    try:
        group.members.remove(me)
    except:
        return redirect(reverse('group:explore'))
    return redirect(reverse('group:explore'))

def accept_join_group_invitation(request, group_id):
    me = User.objects.get(id=request.user.id)
    group = Group.objects.get(id=group_id)
    join_group_invitation = GroupJoinInvitation.objects.get(group=group, invitee=me)
    group.members.add(me)
    join_group_invitation.delete()
    return redirect(reverse('group:view', kwargs={'group_id': group_id}))

def reject_join_group_invitation(request, group_id):
    me = User.objects.get(id=request.user.id)
    group = Group.objects.get(id=group_id)
    join_group_invitation = GroupJoinInvitation.objects.get(group=group, invitee=me)
    join_group_invitation.delete()
    return redirect(reverse('group:view', kwargs={'group_id': group_id}))
