from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from betterforms.multiform import MultiModelForm
from .models import Profile


class UserProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['nickname','genre_Action','genre_Adventure','genre_Animation','genre_Comedy','genre_Crime','genre_Documentary','genre_Drama','genre_Family','genre_Fantasy','genre_Horror','genre_Music','genre_Mystery','genre_Romance','genre_SF','genre_Thriller','genre_War','genre_Western',]
    labels = {
        'nickname': '닉네임',
    }
    
class UserCreationMultiForm(MultiModelForm):
  form_classes = {
    'user': UserCreationForm,
    'profile': UserProfileForm,
  }