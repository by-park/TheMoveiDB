from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserCreationMultiForm
from .forms import UserProfileForm
from django.http import QueryDict
from .models import Profile 
from django.views.decorators.http import require_http_methods

# Create your views here.
def login(request):
  if request.method == "POST":
    forms = AuthenticationForm(request, request.POST)
    if forms.is_valid():
      auth_login(request, forms.get_user())
    return redirect('home')
  else:
    forms = AuthenticationForm()
    return render(request, 'account/login.html', {'forms':forms})

@login_required
def logout(request):
  auth_logout(request)
  return redirect('home')

def signup(request):      
  if request.method == "POST":
    genres = ['액션', '어드벤처', '애니메이션', '코미디', '범죄', '다큐멘터리', '드라마', '가족', '판타지', '공포', '음악', '미스터리', '로맨스' , 'SF', '스릴러', '전쟁', '서부']
    genres_en = ['genre_Action','genre_Adventure','genre_Animation','genre_Comedy','genre_Crime','genre_Documentary','genre_Drama','genre_Family','genre_Fantasy','genre_Horror','genre_Music','genre_Mystery','genre_Romance','genre_SF','genre_Thriller','genre_War','genre_Western']
    post = dict(request.POST)
    be_forms = {}
    be_forms['csrfmiddlewaretoken'] = post['csrfmiddlewaretoken'][0]
    be_forms['user-username'] = post['username'][0]
    be_forms['profile-nickname'] = post['nickname'][0]
    be_forms['user-password1'] = post['password1'][0]
    be_forms['user-password2'] = post['password2'][0]
    for genre in range(len(genres)):
      if genres[genre] in post:
        be_forms['profile-' + genres_en[genre]] = 'on'
    forms = QueryDict('', mutable=True)
    forms.update(be_forms)
    # 넘어온 거 회원가입 체크할 때는 user form이랑 profile form이랑 둘 다 체크 필요
    forms = UserCreationMultiForm(forms)
    if forms.is_valid():
      user = forms['user'].save()
      profile = forms['profile'].save(commit=False)
      profile.user = user
      profile.save()
      auth_login(request, user)
      return redirect('home')
  else:
    # 보내줄 때는 이 form만 있어도 됨
    forms = UserProfileForm()
  return render(request, 'account/signup.html', {'forms' : forms})

@login_required
def delete(request):
  if request.method == "POST":
    request.user.delete()
    return redirect('accounts:signup')
  else:
    return render(request, 'account/delete.html')

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'account/profile.html', {'profile':profile})

@login_required
@require_http_methods(["GET", "POST"])
def change_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
        return redirect('account:profile')
    else:
        form = UserProfileForm
        return render(request, 'account/change_profile.html', {'profile':profile, 'profile_form': profile_form})
    
