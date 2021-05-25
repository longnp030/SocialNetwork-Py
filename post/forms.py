from django import forms

from .models import *
from user.models import *

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', ]

class ImageUploadForm(forms.ModelForm):
    image = forms.ImageField(
        max_length=100, required=True,
        widget=forms.FileInput
    )
    
    class Meta:
        model = Image
        fields = ['image', ]
    
class PostAddImageForm(forms.ModelForm):
    images = forms.ModelMultipleChoiceField(
        queryset=Image.objects.all(),
        required=False,
    )
    class Meta:
        model = Post
        fields = ['images', ]

class TagFriendToPostForm(forms.ModelForm):
    tagged_friends = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False
    )
    class Meta:
        model = Post
        fields = ['tagged_friends', ]

class PostEditForm(forms.ModelForm):
    images = forms.ModelMultipleChoiceField(
        queryset=Image.objects.all(),
        required=False,
    )
    class Meta:
        model = Post
        fields = ['receiver', 'text', 'images', 'tagged_friends', ]