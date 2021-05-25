from django import forms

from .models import *


class GroupChatAddMemberForm(forms.ModelForm):
    inviter = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput()
    )
    invitee = forms.ModelChoiceField(
        queryset=User.objects.all(),
    )
    groupchatbox = forms.ModelChoiceField(
        queryset=GroupChatBox.objects.all(),
        widget=forms.HiddenInput()
    )
    class Meta:
        model = JoinGroupChat
        fields = ['invitee', 'inviter', 'groupchatbox',]

class ChangeChatNameForm(forms.ModelForm):
    creator = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput()
    )
    name = forms.CharField(max_length=100, required=True)
    class Meta:
        model = GroupChatBox
        fields = ['creator', 'name', ]

