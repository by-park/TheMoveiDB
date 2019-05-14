from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import UserCreationMultiForm

# Create your views here.
def login(request):
  if request.method == "POST":
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
    return redirect('posts:list')
  else:
    form = AuthenticationForm()
    return render(request, 'account/login.html', {'form':form})

def logout(request):
  auth_logout(request)
  return redirect('posts:list')

def signup(request):
  if request.method == "POST":
    form = UserCreationMultiForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('home')
  else:
    form = UserCreationMultiForm()
  return render(request, 'account/signup.html', {'form' : form})

def delete(request):
  if request.method == "POST":
    request.user.delete()
    return redirect('accounts:signup')
  else:
    return render(request, 'account/delete.html')