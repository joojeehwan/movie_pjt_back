from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from rest_framework import serializers

from .models import Review, Comment, Hashtag   # 20211110 Hastag 기능 추가
from .forms import ReviewForm, CommentForm
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ReviewistSerializer


@api_view(['GET', 'POST'])  # 필수로 decorator 작성해야함
@permission_classes([AllowAny])
def index(request):    
    # 1. 전체 조회
    if request.method == 'GET':
        reviews = get_list_or_404(Review)        
        print(reviews)
        serializer = ReviewistSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        pass
    











@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            # 20211110 Hastag 기능 추가
            for word in review.content.split():                
                if word[0] == '#':
                    # 2021117 Hashtag 이미 있으면 count 개수 늘리는 로직 추가
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    review.hashtags.add(hashtag)
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_GET
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user.is_authenticated:
        if request.user == review.user: 
            review.delete()
            # return redirect('articles:index')
            # 200
    # return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                # 20211110 Hastag 기능 추가
                review.hashtags.clear()    # 지우고 새로 등록
                for word in review.content.split():                
                    if word[0] == '#':
                        # 2021117 Hashtag 이미 있으면 count 개수 늘리는 로직 추가
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        review.hashtags.add(hashtag)
                return redirect('articles:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('articles:index')
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


# 20211110 Hastag 기능 추가
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    reviews = hashtag.review_set.order_by('-pk')
    context = {
        'hashtag': hashtag,
        'reviews': reviews,
    }
    return render(request, 'articles/hashtag.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            isLiked = False
        else:
            review.like_users.add(user)
            isLiked = True
        # return redirect('community:index')
        context = {
            'isLiked': isLiked,
            'likeCnt': review.like_users.count()
        }
        return JsonResponse(context)
    # return redirect('accounts:login')
    return HttpResponse(status=401)


