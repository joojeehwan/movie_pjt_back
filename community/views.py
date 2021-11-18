from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Review, Comment, Hashtag   # 20211110 Hastag 기능 추가
from .serializers import ReviewistSerializer, ReviewSerializer, CommentSerializer


@api_view(['GET', 'POST'])  # 필수로 decorator 작성해야함
@permission_classes([AllowAny])
def index(request):    
    # 1. 전체 조회
    if request.method == 'GET':
        page_number = request.GET.get('page')
        reviews = Review.objects.order_by('-pk')     
        paginator = Paginator(reviews, 10)
        page_obj = paginator.get_page(page_number)
        serializer = ReviewistSerializer(page_obj, many=True)        
        # data = serializer.data
        return Response(serializer.data)

    # 2. 글 작성    
    elif request.method == 'POST':
        hashtag_list = []
        serializer = ReviewSerializer(data=request.data)                
        if serializer.is_valid(raise_exception=True):
            for word in set(serializer.data.get('content').split()):
                if word[0] == '#':
                     # 2021117 Hashtag 이미 있으면 count 개수 늘리는 로직 추가
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    if created is False:
                        hashtag.count += 1
                        hashtag.save()
                                        
                    hashtag_list.append(hashtag.content)               
            
            serializer.save(user=request.user)#, hashtag=hashtag_list)    ## 되나 확인하기!!!!!!!!!!!!!!!
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        review.click += 1
        review.save()
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELELTE':
        review.delete()
        data = {
            'delete': f'데이터 {review_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 20211110 Hastag 기능 추가
            review.hashtags.clear()    # 지우고 새로 등록
            for word in review.content.split():                
                if word[0] == '#':
                    # 2021117 Hashtag 이미 있으면 count 개수 늘리는 로직 추가
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    if created is False:
                        hashtag.count += 1
                        hashtag.save()
                    review.hashtags.add(hashtag)
            return Response(serializer.data)    # 200으로 return


# 20211110 Hastag 기능 추가
@api_view(['GET'])  # 필수로 decorator 작성해야함
@permission_classes([AllowAny])
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    reviews = hashtag.review_set.order_by('-pk')
    context = {
        'hashtag': hashtag,
        'reviews': reviews,
    }
    return JsonResponse(context)    


# 댓글 조회, 생성
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comment_index(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(review_pk=review_pk).order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 삭제, 수정
@api_view(['DELETE', 'PUT'])
@permission_classes([AllowAny])
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'DELETE':
            comment.delete()
            data = {
            'delete': f'데이터 {comment_pk}번이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    data = {
        'Unauthorized': '권한이 없습니다.'
    }
    return Response(data, status=status.HTTP_403_FORBIDDEN)
