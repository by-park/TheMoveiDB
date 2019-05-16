from django.urls import path
from . import views

app_name = 'movei'

urlpatterns = [
  path('detail/<int:movie_id>/', views.detail, name="detail"),
  path('search/', views.search, name="search"),
  path('comment/<int:movie_id>/create/', views.create, name="create"),
  path('comment/<int:comment_id>/update/', views.update, name="update"),
  path('comment/<int:comment_id>/delete/', views.delete, name="delete"),
]