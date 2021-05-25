from django import forms

from .models import *

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'cover_image', 'description', 'privacy', ]

class GroupPostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []

class GroupEditForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ['members', 'posts']

class GroupInvitationForm(forms.ModelForm):
    group = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Group.objects.all())
    inviter = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=User.objects.all())
    class Meta:
        model = GroupJoinInvitation
        fields = ['invitee', 'group', 'inviter']
