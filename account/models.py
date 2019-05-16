from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  nickname = models.CharField(max_length=40,blank=True)
  genre_Action = models.BooleanField(default=True)
  genre_Adventure = models.BooleanField(default=True)
  genre_Animation = models.BooleanField(default=True)
  genre_Comedy = models.BooleanField(default=True)
  genre_Crime = models.BooleanField(default=True)
  genre_Documentary = models.BooleanField(default=True)
  genre_Drama = models.BooleanField(default=True)
  genre_Family = models.BooleanField(default=True)
  genre_Fantasy = models.BooleanField(default=True)
  genre_Horror = models.BooleanField(default=True)
  genre_Music = models.BooleanField(default=True)
  genre_Mystery = models.BooleanField(default=True)
  genre_Romance = models.BooleanField(default=True)
  genre_SF = models.BooleanField(default=True)
  genre_Thriller = models.BooleanField(default=True)
  genre_War = models.BooleanField(default=True)
  genre_Western = models.BooleanField(default=True)
  
  def __str__(self):
    return f"{self.user.id} / {self.user.username} / {self.nickname}"