# pip install openpyxl 필요
# 참고 사이트: https://bluese05.tistory.com/37
# title_ko, title_en, year, genre_Action 등등 장르들 데이터 들어있는 엑셀 파일

TMDB_KEY = '' # API 키를 입력할 부분!

import openpyxl
import json
import requests

# 엑셀파일 열기
wb = openpyxl.load_workbook('C:/Users/student/Downloads/Moveidbexcel_190514_rating_divided_genres.xlsx')
 
# 현재 Active Sheet 얻기
ws = wb.active
# ws = wb.get_sheet_by_name("Sheet1")

# 장르 목록
movie_list = []

b = [False, True]

# 영화 정보를 읽기
index = 1
for r in ws.rows:
    # url 가져오기
    movie_name = r[1].value
    tmdb_url = "https://api.themoviedb.org/3/search/movie"
    tmdb_params = {
        'api_key': TMDB_KEY,
        'query': movie_name,
        'language': 'ko'
    }
    tmdb_res = requests.get(tmdb_url, params=tmdb_params).json()['results']
    if len(tmdb_res) < 1:
        continue
    else:
        tmdb_res = tmdb_res[0]
        if tmdb_res['poster_path'] == None:
            continue
        else:
            poster_path = 'https://image.tmdb.org/t/p/w500' +tmdb_res['poster_path']
            
            movie_list.append({"pk": index, "model":"movei.movei", "fields":{
             "title_ko": r[1].value, "title_en":r[2].value, "year":r[3].value, "poster_url":poster_path,
             "genre_Action": b[r[4].value], "genre_Adventure":b[r[5].value],
             "genre_Animation":b[r[6].value], "genre_Comedy":b[r[7].value],
             "genre_Crime":b[r[8].value], "genre_Documentary":b[r[9].value],
             "genre_Drama":b[r[10].value], "genre_Family":b[r[11].value],
             "genre_Fantasy":b[r[12].value], "genre_Horror":b[r[13].value],
             "genre_Music":b[r[14].value], "genre_Mystery":b[r[15].value],
             "genre_Romance":b[r[16].value], "genre_SF":b[r[17].value],
             "genre_Thriller":b[r[18].value], "genre_War":b[r[19].value],
             "genre_Western":b[r[20].value]}})
            
            index += 1
    
 
    print(index, r[1].value)
 
# json 파일 저장
with open('C:/Users/student/Downloads/Moveidbexcel_190514_rating_divided_genres_poster_url.json', 'w') as f:
     json.dump(movie_list, f)
# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
