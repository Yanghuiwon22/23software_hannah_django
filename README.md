## 수업 내용 복습하기
# 장고 1주차: windows에서 파이썬 가상환경 만들기
https://github.com/EthanSeok/softeng_2023_django

# 장고 1주차 : 장고 프로젝트 시작하기
1. 장고 내 기본 파일 만들기 ( 스페이스를 치고 점을 찍어야 한다.)

        django-admin startproject softeng_2023_prj .

잘 만들었는지 확인하려면 

        dir

2. 서버 돌리고 주소로 들어가기<br>

        python manage.py runserver

돌리고 나오는 http://127.0.0.1:8000/ 으로 들어간다.

3. 관리자 페이지 DB만들기

        python manage.py migrate

잘 만들었는지 확인하면 db.sqlite3 이 생성되는지 보면 된다.

        dir

- 서버 죽이기 (ctrl + C)

4. 관리자 계정 만들기

        python manage.py createuser

차례대로 유저이름, 이메일, 비밀번호를 입력하면 된다.<br>
비밀번호는 화면에 표시되지 않지만 입력되고 있는것이다. 

- 다시 서버 돌리기

        python manage.py runserver
   










