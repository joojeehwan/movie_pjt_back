from django.contrib import admin
from .models import Actor, Genre, Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    exclude = ('genres','director', 'actors')
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie, MovieAdmin)