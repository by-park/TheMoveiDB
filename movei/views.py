import os
import random
import requests
from django.shortcuts import render

# Create your views here.

moveiName = random.choice(['스파이더맨'])
moveipubDate = "2002"

naver_url = "https://openapi.naver.com/v1/search/movie.json"

naver_headers = {
  'X-Naver-Client-Id': os.getenv('NAVER_ID'),
  'X-Naver-Client-Secret': os.getenv('NAVER_SECRET')
}

naver_params = {
  'query' : moveiName,
  'display' : 100
}

# naver_res = requests.get(naver_url, headers = naver_headers, params = naver_params)

# for item in naver_res.json()["items"]:
#   if item["title"] == '<b>' + moveiName + '</b>' and item["pubDate"] == moveipubDate:
#     print(item)
  

def home(request):
    return render(request, 'movei/home.html')
  
def detail(request):
  return render(request, 'movei/detail.html')

