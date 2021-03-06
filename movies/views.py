from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from requests.api import post
from .serializers import MovieSerializer, MovieListSerializer
from .models import Actor, Genre, Movie
from community.models import Hashtag # 2021117 Hashtag로 영화 검색하기

from django.db.models import F, Q

import requests
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import random

API_KEY = '107e0f67f66553e1c7064118ed5abfaa'

@api_view(['GET'])
@permission_classes([AllowAny])
# 2021117 영화 데이터 수집하기
#  admin만 영화 데이터를 등록할 수 있다.(수정하기)
def saveMovieDatas(request):
    #  admin만 영화 데이터를 등록할 수 있어야 한다.(수정하기)
    print(request.data.get('id'))
    # if request.data.get('id') == 'admin':
    if True:
        # 장르 테이블 
        response = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR')
        response = response.json().get('genres')
        for data in response:
            genre = Genre(pk=data.get('id'), name=data.get('name'))
            genre.save()

        # 인기 영화 
        response = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR')
        response = response.json().get('results')        

        for movie in response:
            tmdb_id =  movie.get('id')
            if Movie.objects.filter(tmdb_id=tmdb_id).count() == 0:  

                poster = movie.get('poster_path')
                if poster is None:
                    poster = 'https://penmadsidrap.com/uploads/blog_image/default.jpg'
                else:
                    poster = 'https://image.tmdb.org/t/p/w300/'+poster 

                data = Movie(
                        tmdb_id = movie.get('id'),
                        title = movie.get('title'),
                        release_date = movie.get('release_date') or datetime.date(1999,12,31),
                        popularity = movie.get('popularity') or 0,
                        vote_count = movie.get('vote_count') or 0,
                        vote_average = movie.get('vote_average') or 0,
                        overview = movie.get('overview') or 'overview...',
                        poster_path = poster #'https://image.tmdb.org/t/p/w300/'+movie.get('poster_path') 
                        )
                data.save()
            else:
                data = Movie.objects.get(tmdb_id=tmdb_id)
                data.popularity = movie.get('populartiy') or 0
                data.vote_count = movie.get('vote_count') or 0
                data.vote_average = movie.get('vote_average') or 0
                data.save()


            data.genres.set(movie.get('genre_ids'))        
            # 영화 감독, 배우 정보         
            response = requests.get(f'https://api.themoviedb.org/3/movie/{tmdb_id}/credits?api_key={API_KEY}&language=ko-KR')
            cast_list = response.json().get('cast')
            actor_list = []
            for cast in cast_list:
                id = cast.get('id')
                name = cast.get('name')            
                if Actor.objects.filter(pk=id).count() == 0:
                    actor = Actor(pk=id, name=name)
                    actor.save()
                actor_list.append(id)  
            data.actors.set(actor_list)

            crew_list = response.json().get('crew')
            for crew in crew_list:            
                if crew.get('job') == 'Director':
                    data.director = crew.get('name')
                    data.save()                
                    break     
        
        return Response({ 'message': '데이터 등록 완료'})
    

def search(query, num=1):
    #  admin만 영화 데이터를 등록할 수 있어야 한다.(수정하기)
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&page=1&include_adult=false&query={query}')
    total_num = response.json().get('total_results')
    response_data = response.json().get('results')
    
    movie = None
    total_num = min(total_num, num)
    for i in range(total_num):    
        data = response_data[i]
        if Movie.objects.filter(tmdb_id=data.get('id')).count() > 0:
            continue

        poster = data.get('poster_path')
        if poster is None:
            poster = 'https://penmadsidrap.com/uploads/blog_image/default.jpg'
        else:
            poster = 'https://image.tmdb.org/t/p/w300/'+poster
        
        movie = Movie(
                tmdb_id = data.get('id'),
                title = data.get('title'),
                release_date = data.get('release_date') or datetime.date(1999,12,31),
                popularity = data.get('popularity') or 0,
                vote_count = data.get('vote_count') or 0,
                vote_average = data.get('vote_average') or 0,
                overview = data.get('overview') or 'overview...',
                poster_path = poster # f'https://image.tmdb.org/t/p/w300/{poster}'
                )
        movie.save()

        movie.genres.set(data.get('genre_ids')) 
        tmdb_id = data.get('id')       
        # 영화 감독, 배우 정보         
        response = requests.get(f'https://api.themoviedb.org/3/movie/{tmdb_id}/credits?api_key={API_KEY}&language=ko-KR')
        cast_list = response.json().get('cast')
        actor_list = []
        for cast in cast_list:
            id = cast.get('id')
            name = cast.get('name')            
            if Actor.objects.filter(pk=id).count() == 0:
                actor = Actor(pk=id, name=name)
                actor.save()
            actor_list.append(id)  
        movie.actors.set(actor_list)

        crew_list = response.json().get('crew')
        for crew in crew_list:            
            if crew.get('job') == 'Director':
                movie.director = crew.get('name')
                movie.save()                
                break
    
    return movie 

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
        # 데이터 베이스에 있으면 그거 출력하고
        if Movie.objects.filter(Q(title__icontains=movieNm)).count() > 0:
            movie = Movie.objects.filter(Q(title__icontains=movieNm)).first()

        # 없으면 tmdb사용해서 검색
        else:
            movie = search(movieNm) #  admin만 영화 데이터를 등록할 수 있어야 한다.(수정하기)
            if movie is None: 
                data = {'message': f'{movieNm}검색결과가 없습니다.'}    
                return JsonResponse(data, content_type="applications/json", status=400)    
        
        movie_data = {            
            'title': movie.title,
            'poster_path': movie.poster_path,     
            'tmdb_id': movie.tmdb_id,
            }
        movies.append(movie_data) 
    return JsonResponse(movies, safe=False)


@api_view(['GET'])  # 필수로 decorator 작성해야함
@permission_classes([AllowAny])
def searchHashtagMovies(request, hashtag_rank):
    hashtags = Hashtag.objects.order_by('-count')
    movies = []
    if hashtag_rank > len(hashtags):
        # 에러 
        data = {'error': f'{hashtag_rank} 랭크의 해시태그가 존재하지 않습니다.'}        
        return JsonResponse(data, content_type="applications/json", status=400)
    else:
        movie_query = hashtags[hashtag_rank-1].content.replace('#', '')
        # search(movie_query, 10) #  admin만 영화 데이터를 등록할 수 있어야 한다.(수정하기)

        movies_list = Movie.objects.filter(Q(title__icontains=movie_query)|Q(overview__icontains=movie_query))        
        if movies_list.count() > 0:
            movie_count = min(movies_list.count(), 10)
            # print(random.sample(list(movies_list), movie_count))
            movies_list = random.sample(list(movies_list), movie_count)
            for movie in movies_list:
                movie_data = {                     
                    'title': movie.title,
                    'poster_path': movie.poster_path,     
                    'tmdb_id': movie.tmdb_id,
                }
                movies.append(movie_data)   
        else:            
           # 검색 결과 없으면 에러            
            data = {'error': f'#{movie_query}와 연관된 영화가 존재하지 않습니다.'}        
            return JsonResponse(data, content_type="applications/json", status=400)

    results = {'hashtag': movie_query, 'movies': movies} 
    return JsonResponse(results, safe=False)


@api_view(['GET'])  # 필수로 decorator 작성해야함
@permission_classes([AllowAny])
def detail(request, movie_pk):    
    movie = get_object_or_404(Movie, tmdb_id=movie_pk)
    actors_list = []
    genres_list = []
      
    for actor in movie.actors.all():
        actors_list.append(Actor.objects.get(pk=actor.id).name)
        
    for genre in movie.genres.all():
        genres_list.append(Genre.objects.get(pk=genre.id).name)

    movie = {            
        'title': movie.title,
        'poster_path': movie.poster_path,     
        'release_date': movie.release_date,
        'vote_average': movie.vote_average,
        'overview': movie.overview,
        'director': movie.director,
        'genres_list': genres_list,
        'actors_list': actors_list,            
        }

    return JsonResponse(movie, safe=False)


@api_view(['GET'])  # 필수로 decorator 작성해야함
@permission_classes([AllowAny])    
def searchTopRatedMovies(request):
    # 평점순 정렬하여 10개 
    movies = Movie.objects.order_by('-vote_average')[:10]
    results = []

    for movie in movies:
        movie = {            
                'title': movie.title,
                'poster_path': movie.poster_path,     
                'tmdb_id': movie.tmdb_id 
            }
        results.append(movie)       
    return JsonResponse(results, safe=False)



@api_view(['GET'])  # 필수로 decorator 작성해야함
@permission_classes([AllowAny])    
def searchBarMovies(request, movie_query):
    results = []
    check_list = [] # 중복 체크용
    movies = Movie.objects.filter(Q(title__icontains=movie_query)|Q(overview__icontains=movie_query))            
    for movie in movies:
        if movie.tmdb_id in check_list:
            continue
        check_list.append(movie.tmdb_id)

        movie = {            
                'title': movie.title,
                'poster_path': movie.poster_path,     
                'tmdb_id': movie.tmdb_id 
            }
        results.append(movie)       
        
    
    genre_id = Genre.objects.filter(name=movie_query)
    for g_id in genre_id:  # 어차피 한 개지만 없는 경우 넘어가기 위해서        
        genre = get_object_or_404(Genre, id=g_id.id)
        genre_movies = genre.movie_set.filter(genres=genre.id)
        for genre_movie in genre_movies:
            if genre_movie.tmdb_id in check_list:
                continue
            check_list.append(genre_movie.tmdb_id)

            genre_movie = {            
                'title': genre_movie.title,
                'poster_path': genre_movie.poster_path,     
                'tmdb_id': genre_movie.tmdb_id 
                }
            results.append(genre_movie)
    
    actor_id = Actor.objects.filter(name__icontains=movie_query)
    for a_id in actor_id:  # 어차피 한 개지만 없는 경우 넘어가기 위해서        
        actor = get_object_or_404(Actor, id=a_id.id)
        actor_movies = actor.movie_set.filter(actors=actor.id)
        for actor_movie in actor_movies:            
            if actor_movie.tmdb_id in check_list:                
                continue
            check_list.append(actor_movie.tmdb_id)

            actor_movie = {            
                'title': actor_movie.title,
                'poster_path': actor_movie.poster_path,     
                'tmdb_id': actor_movie.tmdb_id 
                }
            results.append(actor_movie)                       
    
    return JsonResponse(results, safe=False)


@api_view(['GET'])  # 필수로 decorator 작성해야함
@permission_classes([AllowAny])    
def searchAllMovies(request):
    movies = Movie.objects.all()

    serializer = MovieListSerializer(movies, many=True)        
    return Response(serializer.data)
    # return JsonResponse(list(movies), safe=False)


