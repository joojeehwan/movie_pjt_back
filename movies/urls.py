from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # path('', views.index, name='index'),
    # 1114 - 1. 주간 박스오피스 영화
    path('searchWeeklyBoxOfficeMovies/', views.searchWeeklyBoxOfficeMovies
        , name='searchWeeklyBoxOfficeMovies'),
    # 1117 - 2. 해시태그로 영화 검색
    path('searchHashtagMovies/<int:hashtag_rank>/', views.searchHashtagMovies),
    # 1117 - 3. 영화 세부 정보 검색 
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('searchTopRatedMovies/', views.searchTopRatedMovies),
    path('saveMovieDatas/', views.saveMovieDatas, name='saveMovieDatas'),
]
