# 사용하기 전에..
## - 요구사항
1. python 3.11
2. java-17
## - 환경 구축 (Windows 기준)
### ※ 경로, 환경 변수 등 충돌 방지 위해 본 Repository의 이름대로 설정하는 것을 권장
1. 프로젝트 폴더 만들기
2. 명령 프롬프트 실행
3. 프로젝트 폴더로 현재 경로 이동
4. `python venv -m "가상환경이름"` 명령어로 가상환경 생성
5. `"가상환경이름"\Scripts\activate.bat` 명령어로 가상환경 실행
6. `pip install` 명령어로 아래 라이브러리 설치
- `django`, `djangorestframework`, `sklearn`,`konlpy`, `gensim`, `numpy`, `pandas`, `scipy==1.10.1`
7. `django-admin startproject "프로젝트이름" .` 명령어로 현재 경로에 프로젝트 만들기
8. `python manage.py startapp "앱이름"` 명령어로 Django App 만들기
9. 본 Repository의 source file들을 경로에 맞게 이동 및 덮어쓰기 <br>
※ 덮어쓰기 전에, 기존 "프로젝트이름"/settings.py SECRET_KEY 변수는 그대로 둘 것 염두!!
10. 소스 파일 확인 후 "프로젝트이름"이 들어갈 곳, "앱이름"이 들어갈 곳, 경로 등 확인 후 수정
11. `python manage.py makemigrations`, `python manage.py migration` 명령어를 통해 DB 스키마 마이그레이션 파일 생성
12. `python manage.py runserver "IP:Port"` 명령어로 server 실행