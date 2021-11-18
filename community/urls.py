from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),    
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/comments/', views.comment_index, name='create_comment'),    
    path('<int:comment_pk>/comments/detail/', views.comment_detail, name='create_comment'),    

    # 20211110 Hastag 기능 추가
    path('<int:hash_rank>/hashtag/', views.hashtag, name='hashtag'),    
]
