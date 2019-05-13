from django.urls import path
from . import views

app_name = 'movei'

urlpatterns = [
  path('detail/', views.detail, name="detail")
]