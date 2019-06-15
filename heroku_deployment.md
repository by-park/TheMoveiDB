# Heroku deployment with Django (Heroku 배포 관련 사항)

2019-06-15

## 1. Heroku 회원가입 및 배포를 원하는 장고 프로젝트로 이동

구름 IDE에서 Heroku 연동에 실패하여, git clone을 통해 c9 IDE에서 새로 작업하였다.

## 2. 가상환경 설정 및 필요한 package들 미리 설치

Heroku에 배포시 필요한 패키지들을 다 freeze해서 한번에 설치되도록 할 것이다.
현재 프로젝트에서 필요한 패키지들은 django, restframework, betterforms, requests가 있었다.

## 3. 배포에 필요한 package 설치

`pip install django-heroku`
`pip install gunicorn`

## 4. `settings.py` 다음의 내용 추가

가장 상단 부분에 `import django_heroku`를 추가한다.

가장 하단 부분에 `django_heroku.settings(locals())`를 추가한다.

## 5. 새 파일 `Procfile` 생성

확장자는 없고, 가장 상위 폴더 아래에 생성한다.

`web: gunicorn 프로젝트이름.wsgi` 를 작성한다.

프로젝트의 이름을 모르면 `wsgi.py` 파일로 가서 프로젝트이름.settings 찾는다.


## 5. 새 파일 `runtime.txt` 생성

가장 상위 폴더 아래에 생성하고, `python-3.6.7`를 작성한다.

## 6. freeze를 이용하여 필요한 패키지들 한 번에 정리하기

`pip freeze > requirements.txt` 이 명령어를 그대로 입력하면 현재 설치된 패키지들이 모두 requirements.txt에 저장된다.

## 7. Heroku 접속

`heroku login` 을 입력해서 나오는 창에 아이디, 비밀번호를 작성하여 로그인한다.
(로그인 실패할 경우 heroku login --interactive)

## 8. Heroku app 생성

`heroku create 원하는 이름` 을 작성한다.

기존에 존재하는 이름을 작성할 수 없기 때문에 유니크한 이름을 지어야 한다.

## 9. git을 이용하여 배포

`git add .`, `git commit -m "커밋 메세지"` 후에 `git push heroku master`로 업로드

## 10. 배포 후 DB 생성 및 Django 관리자 계정 생성

`heroku run python manage.py migrate`

`heroku run python manage.py createsuperuser`

migrate시 충돌이 나는 등 오류가 생기는 경우, `heroku run bash`로 bash를 켜서 migrations 파일들을 삭제하면 된다.

`rm 00001_이름.py` 을 이용하여 이런 형식의 파일들을 삭제한다.

본 프로젝트는 fixtures에 존재하는 파일을 DB에 추가해야했기 때문에 `heroku run python manage.py loaddata 이름.json` 도 활용하였다. 

## 11. 환경 변수 활용하기

구름 IDE나 c9 IDE의 경우 `vi ~/.bashrc` 를 활용할 수 있지만, Heroku의 경우 해당 파일이 존재하지 않는다.

`heroku config:set NAVER_ID=??? NAVER_SECRET=??? TMDB_KEY=???` 을 활용하였다.

이렇게 명령어를 쳐도 되고, 혹은 Heroku의 app 설정 화면에서도 직접 추가, 수정이 가능하다.

(추가 정보는 https://devcenter.heroku.com/articles/config-vars)

추가한 환경 변수는 Django 프로젝트의 `views.py` 등에 다음과 같이 활용하면 된다.

```python
import os

variable_name = os.environ.get('TMDB_KEY', True)
```

**디테일한 작업이 필요한 경우에 `heroku run bash`를 활용하면 좋다**