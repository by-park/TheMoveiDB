from django.urls import path
from . import views

app_name = 'etc'

urlpatterns = [
  path('', views.about, name="about"),
]