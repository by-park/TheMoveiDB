from django.db import models
from django.conf import settings

# Create your models here.
class Movei(models.Model):
  title_ko = models.CharField(max_length=200)
  title_en = models.CharField(max_length=200)
  year = models.IntegerField()
  poster_url = models.TextField(blank=False)
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
  
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "like_movei", blank = True)
  
  def __str__(self):
    return f"{self.year} / {self.title_ko} / {self.title_en}"
  
class Comment(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  movei = models.ForeignKey(Movei, on_delete = models.CASCADE)
  content = models.CharField(max_length = 140)