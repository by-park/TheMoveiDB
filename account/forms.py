from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from betterforms.multiform import MultiModelForm
from .models import Profile


class UserProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['genre_Action','genre_Adventure','genre_Animation','genre_Comedy','genre_Crime','genre_Documentary','genre_Drama','genre_Family','genre_Fantasy','genre_Horror','genre_Music','genre_Mystery','genre_Romance','genre_SF','genre_Thriller','genre_War','genre_Western',]
    labels = {
      'genre_Action':'액션',
      'genre_Adventure':'어드벤처',
      'genre_Animation':'애니메이션',
      'genre_Comedy':'코미디',
      'genre_Crime':'범죄',
      'genre_Documentary':'다큐멘터리',
      'genre_Drama':'드라마',
      'genre_Family':'가족',
      'genre_Fantasy':'판타지',
      'genre_Horror':'공포',
      'genre_Music':'음악',
      'genre_Mystery':'미스터리',
      'genre_Romance':'로맨스',
      'genre_SF':'SF',
      'genre_Thriller':'스릴러',
      'genre_War':'전쟁',
      'genre_Western':'서부',
    }
    
class UserCreationMultiForm(MultiModelForm):
  form_classes = {
    'user': UserCreationForm,
    'profile': UserProfileForm,
  }