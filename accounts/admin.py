from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'username')

admin.site.register(User, UserAdmin)
