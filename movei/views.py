import os
import random
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movei
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth.decorators import login_required

# Create your views here.  
def home(request):
    # check = 0
    # movies = [0] * 3
    
        # 선택한 장르를 불러와서 취향 중에서 골라줘야한다.
    if request.user.is_authenticated:
        movie1 = requests.get(f'https://themoveidb.run.goorm.io/api/v1/users/{request.user.id}/').json()
        movie2 = requests.get(f'https://themoveidb.run.goorm.io/api/v1/users/{request.user.id}/').json()
        movie3 = requests.get(f'https://themoveidb.run.goorm.io/api/v1/users/{request.user.id}/').json()
    else:
        movie1 = requests.get('https://themoveidb.run.goorm.io/api/v1/users/2/').json() # 유령 유저 하나 만들어서 default로 잡아줘야한다
        movie2 = requests.get('https://themoveidb.run.goorm.io/api/v1/users/2/').json()
        movie3 = requests.get('https://themoveidb.run.goorm.io/api/v1/users/2/').json()

    movies = [Movei.objects.get(id=movie1['id']), Movei.objects.get(id=movie2['id']), Movei.objects.get(id=movie3['id'])]
        # selected_movies = random.sample(range(1, Movei.objects.count()+1), 3)
    # while check == 0: # 3 개 다 데이터가 있을 때까지 뽑기!
    #     for i in range(3):
    #         movie_name = Movei.objects.get(pk=selected_movies[i]).title_ko
    #         tmdb_url = "https://api.themoviedb.org/3/search/movie"
    #         tmdb_params = {
    #             'api_key': os.getenv('TMDB_KEY'),
    #             'query': movie_name,
    #             'language': 'ko'
    #         }
    #         tmdb_res = requests.get(tmdb_url, params=tmdb_params).json()['results']
    #         if len(tmdb_res) < 1:
    #             break
    #         else:
    #             tmdb_res = tmdb_res[0]
    #             print(tmdb_res)
    #             if tmdb_res['poster_path'] == None:
    #                 break
    #                 # poster_path = static('images/default.jpg')
    #             else:
    #                 poster_path = 'https://image.tmdb.org/t/p/w500' +tmdb_res['poster_path']
    #                 movies[i] = {'title_ko':tmdb_res['title'], 'poster_url':poster_path, 'id':Movei.objects.get(pk=selected_movies[i]).id}
    #                 print(Movei.objects.get(pk=selected_movies[0]).title_ko)
                    
    #     else:
    #         check = 1
    return render(request, 'movei/home.html', {'movies':movies, 'tmdb_key':os.getenv('TMDB_KEY')})
  
def detail(request, movie_id):
    if movie_id == 1234567890:
        return render(request, 'movei/404.html')
    movie = Movei.objects.get(pk=movie_id)
    movie_name = movie.title_ko
    movie_year = movie.year
    tmdb_url = "https://api.themoviedb.org/3/search/movie"
    tmdb_params = {
        'api_key': os.getenv('TMDB_KEY'),
        'query': movie_name,
        'language': 'ko'
    }
    tmdb_res_id = requests.get(tmdb_url, params=tmdb_params).json()['results'][0]['id']
    tmdb_url_detail = f"https://api.themoviedb.org/3/movie/{tmdb_res_id}"
    tmdb_params_detail = {
        'api_key': os.getenv('TMDB_KEY'),
        'language': 'ko'
    }

    tmdb_res_detail = requests.get(tmdb_url_detail, params=tmdb_params_detail).json()
    # print(tmdb_res)
    tmdb_res_detail['poster_path'] = 'https://image.tmdb.org/t/p/w500' +tmdb_res_detail['poster_path']
    tmdb_res_detail['release_date'] = tmdb_res_detail['release_date'][:4]
    tmdb_res_detail['vote_average'] = int(tmdb_res_detail['vote_average'] * 10)
    tmdb_res_detail['vote_average_point'] = tmdb_res_detail['vote_average'] / 100
    tmdb_res_detail['genres'] = tmdb_res_detail['genres'][:3]
    if len(tmdb_res_detail['overview']) > 300:
      tmdb_res_detail['overview'] = tmdb_res_detail['overview'][:280] + '...'
    # movie = {'title_ko':tmdb_res['title'], 'poster_url':poster_path}
    
    naver_url = "https://openapi.naver.com/v1/search/movie.json"
    naver_headers = {
      'X-Naver-Client-Id': os.getenv('NAVER_ID'),
      'X-Naver-Client-Secret': os.getenv('NAVER_SECRET')
    }

    naver_params = {
      'query': movie_name,
      'yearfrom':tmdb_res_detail['release_date'],
      'yearto':tmdb_res_detail['release_date'],
    }
    naver_res = requests.get(naver_url, headers = naver_headers, params = naver_params).json()
    if len(naver_res['items']) < 1:
        naver_res['directors'] = ['감독 정보 없음']
        naver_res['actors'] = ['배우 정보 없음']
    else:
        naver_res['directors'] = naver_res['items'][0]['director'].split('|')[:3]
        naver_res['actors'] = naver_res['items'][0]['actor'].split('|')[:3]
    print(naver_res)
    tmdb_res_detail.update(naver_res)
    like_users = movie.like_users.all()
    if request.user in like_users:
        user_dict = {'liked': True, 'movie_id': movie.id, 'movie_count':len(like_users)}
    else:
        user_dict = {'liked': False, 'movie_id': movie.id, 'movie_count':len(like_users)}
    tmdb_res_detail.update(user_dict)
    return render(request, 'movei/detail.html', tmdb_res_detail)
# {'movei_title':movie['title_ko'], 'poster_url':movie['poster_url'], 'movei_year':movie_year}

def search(request):
    tmdb_url = "https://api.themoviedb.org/3/search/movie"
    tmdb_params = {
        'api_key': os.getenv('TMDB_KEY'),
        'query': request.POST['query'],
        'language': 'ko'
    }
    movie_res = requests.get(tmdb_url, params=tmdb_params).json()['results']
    if len(movie_res) < 1:
        return redirect('movei:detail', 1234567890)
    movie_name = movie_res[0]['title']
    if not Movei.objects.filter(title_ko=movie_name).exists():
        return redirect('movei:detail', 1234567890)
    else:
        movie = Movei.objects.get(title_ko=movie_name)
    return redirect('movei:detail', movie.id)

def create(request, movie_id):
    
    pass

def update(request, comment_id):
    pass

def delete(request, comment_id):
    pass