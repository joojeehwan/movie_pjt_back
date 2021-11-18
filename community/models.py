from django.db import models
from django.conf import settings

# 20211110 Hastag 기능 추가
class Hashtag(models.Model):
    content = models.TextField(unique=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.content

class Review(models.Model):
    title = models.CharField(max_length=100)    
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    click = models.PositiveIntegerField(default=0) # 20211117 조회수 추가
    hashtags = models.ManyToManyField(Hashtag) # 20211110 Hastag 기능 추가    

    def __str___(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
