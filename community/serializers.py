from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Review, Comment


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'title', 'movie_title','click', 'created_at')

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'review')  # 전체 시리얼라이즈
        read_only_fields = ('review',) # 읽기 전용 필드로 사용자한테 데이터 오는 것 아니므로 나중에 보여지기만 하는 것임을 명시


class ReviewSerializer(serializers.ModelSerializer):
    # 특정 게시글 댓글 목록 출력 
    # read_only 속성으로 추가 필드 작성
    # 역참조(1:N관계에서 1인 입장에서)
    
    # 1. PrimaryKeyRelatedField 방법
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # 2. Nested relationships
    # comment_set = CommentSerializer(many=True, read_only=True)

    # 특정 게시글 작성된 댓글 개수 구하기 (article.comment_set.count)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    ## 필드 override 혹은 추가한 경우 'read_only_fields' shortcut사용 할 수 없음
    class Meta:
        model = Review
        fields = ('movie_title', 'title', 'content')

