from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movei.models import Movei
from .serializers import MovieSerializer
from account.models import Profile
import random
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@api_view(['GET'])
def movie_detail(request, movie_id):    
    movie = Movei.objects.get(pk=movie_id)
    serializer = MovieSerializer(movie) #, many=True
    return Response(serializer.data)

genres = ['genre_Action', 'genre_Adventure', 'genre_Animation', 'genre_Comedy', 'genre_Crime', 'genre_Documentary', 
          'genre_Drama', 'genre_Family', 'genre_Fantasy', 'genre_Horror', 'genre_Music', 'genre_Mystery', 'genre_Romance',
         'genre_SF', 'genre_Thriller', 'genre_War', 'genre_Western']

@api_view(['GET'])
def movie_random(request, user_id):
    # 유저 취향을 고려해서 영화 랜덤 추천
    user_genres = []
    user = Profile.objects.get(user_id=user_id) # anonymous는 어떻게 처리?
    # 취향을 돌면서 걔네를 넣은 list에서 랜덤으로 하나 꺼내고, 거기서 또 objects들에서 filter로 여러개 가져와서
    for i in range(len(genres)):
        if eval(f'user.{genres[i]}') != True:
            user_genres.append(i)
    if len(user_genres) == 17:
        movie = Movie.objects.get(id=1) # 클레멘타인으로 바꿀 것!
        serializer = MovieSerializer(movie) #, many=True
        return Response(serializer.data)

    check = 0
    while check == 0:
        # user의 filter 리스트를 돌면서 아니라고 하면 while문 다시 돌기
        movie = Movei.objects.get(id=random.choice(range(1, Movei.objects.count()+1)))
        for i in user_genres:
            if eval(f'movie.{genres[i]}') == True:
                break
        else:
            check = 1
    serializer = MovieSerializer(movie) #, many=True
    return Response(serializer.data)


@login_required        
def check_like(request, movie_id):
    movie = get_object_or_404(Movei, id=movie_id)
    if request.user in movie.like_users.all():
        liked = True
    else:
        liked = False
    return JsonResponse({'liked': liked})

@login_required 
def vue_like(request, movie_id):
    movie = get_object_or_404(Movei, id=movie_id)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
        liked = False
    else:
        movie.like_users.add(request.user)
        liked = True
    return JsonResponse({'liked': liked})