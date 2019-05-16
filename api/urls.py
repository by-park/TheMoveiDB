from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/', views.movie_detail),
    path('users/<int:user_id>/', views.movie_random),
    path('like/<int:movie_id>/', views.vue_like),
    path('check/<int:movie_id>/', views.check_like),
]