from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreationMultiForm
from .forms import UserProfileForm

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

def logout(request):
  auth_logout(request)
  return redirect('home')

def signup(request):
  if request.method == "POST":
    # 넘어온 거 회원가입 체크할 때는 user form이랑 profile form이랑 둘 다 체크 필요
    forms = UserCreationMultiForm(request.POST) #forms = UserProfileForm(request.POST)
    if forms.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('home')
  else:
    # 보내줄 때는 이 form만 있어도 됨
    forms = UserProfileForm()
  return render(request, 'account/signup.html', {'forms' : forms})

def delete(request):
  if request.method == "POST":
    request.user.delete()
    return redirect('accounts:signup')
  else:
    return render(request, 'account/delete.html')