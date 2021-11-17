from django.db import models
from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import login_required
from .models import Movie
from community.models import Hashtag # 2021117 Hashtag로 영화 검색하기

from django.db.models import Max
import random
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse
import requests
import datetime


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)

    #사용자의 요쳥으로 부터 GET메서드로 "page"에 관한 정보를 가져온다.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    #/movies/?page=2 ajax 요청 => json

    if request.headers.get("x-requested-with") == "XMLHttpRequest" :
       data = serializers.serialize("json", page_obj)
       return HttpResponse(data, content_type="applications/json")

    #/movies/ 첫번째 페이지 요청 => html
    else:
        print("HTML") 
        context = { 
            'movies': page_obj,
        }
        return render(request, 'movies/index.html', context)






@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all() 
    context = {
        'movie': movie,
        'genres': genres,
    }
    return render(request, 'movies/detail.html', context)

@login_required
@require_safe
def recommended(request):    
    if request.user.is_authenticated:
        recommendMovies = set()
        # 전체 영화 목록에서 random 10개 추출
        while True:
            if len(recommendMovies) == 10:
                break
            max_id = Movie.objects.all().aggregate(max_id=Max('id'))["max_id"]
            pk = random.randint(1, max_id)
            recommendMovies.add(Movie.objects.get(pk=pk))
        context = {
            'recommendMovies': recommendMovies

        }
        # movies = list(Movie.objects.all())        
        # recommendMovies = random.sample(movies, 10)        
       
        return render(request, 'movies/recommended.html', context)






# 포스터 이미지 받아오기 - 1. 네이버 API
NAVER_URL = 'https://openapi.naver.com/v1/search/movie.json'
CLIENT_SECRET = 'tB6QZ6LzyG'
CLIENT_ID = 'NhnBdNZiKhE0vPj73Foz'
# 포스터 이미지 받아오기 - 2. kakao img API
KAKAO_KEY = '382fa6ad156c258979f116f06f9ceac3'
KAKAO_URL = 'https://dapi.kakao.com/v2/search/image'

# 1114 - 1. 주간 박스오피스 영화
def searchWeeklyBoxOfficeMovies(request):
    movies = []
    KOBIS_URL = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'


    today = datetime.date.today() - datetime.timedelta(weeks=1)  # 일주일전
    today = str(today).replace('-','')    
    params = {
        'key': 'f5eef3421c602c6cb7ea224104795888',
        'targetDt': today,
        'weekGb': '0',  # 주간
    }
    response = requests.get(KOBIS_URL, params).json()
    
    weeklyBoxOfficeList = response['boxOfficeResult'].get('weeklyBoxOfficeList')    
        
    for i in range(10):
        movieNm = weeklyBoxOfficeList[i].get('movieNm')
        # 1. 네이버 영화 thumbnail
        # params = {
        #     'query': movieNm,           
        # }
        # headers = {
        #     'X-Naver-Client-Id': CLIENT_ID,
        #     'X-Naver-Client-Secret': CLIENT_SECRET
        # }
        # response = requests.get(NAVER_URL, headers=headers, params=params).json()
        # poster_path = response.get('items')[0].get('image')

        # # 2. kakao img 검색
        # params = {
        #     'query': f'{movieNm}공식포스터',
        # }
        # headers = {
        #     'Authorization': f'KakaoAK {KAKAO_KEY}'
        # }
        # response = requests.get(KAKAO_URL, headers=headers, params=params).json()
        # if len(response.get('documents')) >= 1:                    
        #     poster_path = response.get('documents')[0].get('image_url')
        # else:
        #     poster_path = ''



 

        # WeeklyBoxOfficeMovie 시리얼라이저 만들기
        
    #     movie = {
    #         'rank': weeklyBoxOfficeList[i].get('rank'), 
    #         'title': movieNm,
    #         'poster_path': ''#poster_path, 
    #         # 'overview': 
    #     }
    #     movies.append(movie)    
    # return JsonResponse(movies, safe=False)

    response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=107e0f67f66553e1c7064118ed5abfaa&language=ko-KR&page=1')
    response = response.json().get('results')

    # 2021117 영화 데이터 수집하기
    # for movie in response:


    return JsonResponse(response, safe=False)



def searchHashtagMovies(request, hashtag_rank):
    hashtags = Hashtag.objects.order_by('-count')
    movies = []
    if hashtag_rank > len(hashtags):
        # 에러 
        data = {'error': f'{hashtag_rank} 랭크의 해시태그가 존재하지 않습니다.'}        
        return JsonResponse(data, content_type="applications/json", status=400)
    else:
        movie_query = hashtags[hashtag_rank-1].content.replace('#', '')
        # print(movie_query)
        # 1. 네이버 영화 
        params = {
            'query': movie_query,           
        }
        headers = {
            'X-Naver-Client-Id': CLIENT_ID,
            'X-Naver-Client-Secret': CLIENT_SECRET
        }
        response = requests.get(NAVER_URL, headers=headers, params=params).json()
        movie_cnt = len(response.get('items'))
        # 검색 결과 없으면 에러
        if movie_cnt <= 0:
            data = {'error': f'제목에 #{movie_query}가 들어간 영화가 존재하지 않습니다.'}        
            return JsonResponse(data, content_type="applications/json", status=400)

        for i in range(movie_cnt):
            poster_path = response.get('items')[i].get('image')
            movieNm = response.get('items')[i].get('title').replace('<b>', '').replace('</b>', '')
            movie = {            
                'title': movieNm,
                'poster_path': poster_path,                
            }
            movies.append(movie)   
    results = {'hashtag': movie_query, 'movies': movies} 
    return JsonResponse(results, safe=False)



