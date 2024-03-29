# README



### 1. 프로젝트 개요

본 프로젝트명은 TheMoveiDB 로 TheMovieDB의 API를 활용한 영화 랜덤 추천 서비스입니다. 앱 주소는 [themoveidb.org](themoveidb.org) 입니다. (마지막 업데이트일 2019-05-16)



### 2. 개발환경

- 구름 IDE 공동 작업 (Linux)
- Django 2.1.7
- Python 3.6.7
- Python Module: django-rest-framework, django-betterforms
- SQLite3



### 3. 서버 배포 환경

- 가비아 도메인 사용
- Heroku (추후 업데이트 예정)



### 4. 서비스 개요

- 랜덤 영화를 추천받기 위해서는 본 서비스의 메인 페이지에 접속하면 됩니다. 로그인하지 않은 경우 모든 장르에서 랜덤으로 추출하고, 로그인한 경우 유저가 선택한 장르 기반으로 추출합니다. 
- 혹은 랜덤 영화를 API를 활용하여 받을 수 있습니다. (CORS headers 기능을 달지 않아서 정식 API로는 활용할 수 없습니다.) API 주소는 /api/v1/movies/{movie_id}/ 를 사용하면 DB에 있는 영화 상세 정보를 받을 수 있으며, /api/v1/users/{user_id}/를 사용하면 특정 유저를 위한 추천 영화 1개 정보를 받을 수 있습니다.
- 영화 정보는 영화진흥위원회의 2019-05-14 기준 청소년 관람불가 외 모든 영화를 엑셀 다운로드하였습니다. 이 중 TMDB API를 활용하여 영화 포스터를 얻을 수 있는 영화만 데이터베이스에 반영하였고, 2019-05-16일 현재 기준 8416 개의 영화가 포함되어있습니다.
- 다운받은 엑셀 데이터를 json으로 변환하기 위해 작성한 파이썬 코드는 'Python_codes' 폴더에 있습니다.



### 5. 서비스 아키텍처

- ERD model (사용한 프로그램: [https://dbdiagram.io/](https://dbdiagram.io/))
![ERD model](https://github.com/BY1994/TheMoveiDB/blob/master/ERD_model.PNG)
- 관리자 페이지 (/admin): 관리자는 영화 수정, 삭제 및 유저 수정 삭제 권한이 있습니다.
- 회원가입, 로그인, 회원탈퇴가 가능합니다.
- 로그인한 유저는 좋아요 기능, 한줄평 작성 기능을 사용할 수 있습니다.
- 회원가입 및 로그인시 비밀번호는 Django Framework 기본 기능으로 모두 암호화 되고 있으며, 데이터베이스에 기록되는 모든 정보는 Django ModelForm을 활용해 유효성 검사를 진행합니다.



### 6. 프로젝트 정보

​	**i. 팀원 정보 및 업무 분담 내역**

		- 박보윤: 욕심가득 개발자. 장고 프레임워크 틀 및 서버 배포를 위한 백엔드
		- 한동훈: 열정가득 개발자. HTML (with Django DTL문법), CSS, JAVASCRIPT 를 활용한 극강의 아름다운 프론트엔드

​	**ii. 목표 서비스 구현 및 실제 구현 정도**

- 프로젝트 주제는 완전 랜덤 영화 추천 프로젝트이며, 실제로 가입한 회원의 장르 선호에 따라 새로운 랜덤 영화 추천을 구현하였습니다. 
- 그 외 필수적인 회원가입, 로그인, 영화 정보 API 요청, 댓글 작성 및 삭제 기능을 추가로 구현하였습니다.

​	**iii. 데이터베이스 모델링**

- Movei: 영화 정보를 저장하기 위한 DB 테이블

- Comment: 유저들이 기록한 한줄평을 저장할 DB 테이블

- Profile: 가입시 지정한 닉네임 및 영화 장르 선택 내용을 저장한 DB 테이블

  자세한 내용은 위의 ERD model 참고

​	**iv. 핵심 기능**

- 영화를 랜덤으로 추천하는 사이트입니다. 회원가입시 혹은 회원정보 변경을 통해 최종 반영한 유저의 장르에 기반해서만 랜덤 영화를 보여줍니다. 랜덤 영화 정보는 장고 서버 내 구축한 api를 통해서 현재 접속한 유저 기반 추천 영화를 json으로 응답합니다.

​	**v. 배포 서버 URL**

- themoveidb.org 도메인은 가비아를 통해 운영중이며, 도메인 유효 기간은 2019-05-13 ~ 2020-05-13 입니다.
- Heroku 도메인은 [https://themoveidb.herokuapp.com/](https://themoveidb.herokuapp.com/) 입니다.

​	**vi. 기타(느낀점)**

- 박보윤: 개발자는 멋진 직업입니다!
- 한동훈: 굳!