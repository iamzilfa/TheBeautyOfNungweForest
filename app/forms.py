from django import forms
from .models import Profile,Photo,Comments
from django.forms import ModelForm,Textarea,IntegerField


class NewPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user','photos','likes']


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','photos']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['posted_by', 'commented_photo','user']
        

