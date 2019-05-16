from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
  path('login/', views.login, name="login"),
  path('logout/', views.logout, name="logout"),
  path('signup/', views.signup, name="signup"),
  path('delete/', views.delete, name="delete"),
  path('profile/', views.profile, name="profile"),
  path('change_profile/', views.change_profile, name="change_profile"),
]