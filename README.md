1. loaddata

   fixtures : 프로젝트 테스트 시 고정된 더미 데이터

   python manage.py loaddata <filename>

   > python manage.py loaddata movies.json

   

2. dumpdata

   python manage.py dumpdata <app_name>[.ModelName] > 

   > python manage.py dumpdata -- indent 4 movies > tests.json

   > 한글 incodng이 깨지므로,  메모장으로 열어서 인코딩 utf-8로 변환해서 다시 저장

- endcoding error 발생시

  >  python -Xutf8 manage.py dumpdata --indent 4 movies > movies.json





-----------------

1. ERD
2. DB fixtures 만들기
3. 
