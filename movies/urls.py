from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # path('', views.index, name='index'),
    # 1114 - 1. 주간 박스오피스 영화
    path('searchWeeklyBoxOfficeMovies', views.searchWeeklyBoxOfficeMovies
        , name='searchWeeklyBoxOfficeMovies'),
    # path('<int:movie_pk>/', views.detail, name='detail'),
    # path('recommended/', views.recommended, name='recommended'),
]
