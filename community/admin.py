from django.contrib import admin
from .models import Review, Comment, Hashtag # 20211110 Hastag 기능 추가 

class ReviewAdmin(admin.ModelAdmin):
    exclude = ('like_users','hashtags', 'click')

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)
# 20211110 Hastag 기능 추가
admin.site.register(Hashtag)