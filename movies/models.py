from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    tmdb_id = models.IntegerField(unique=True)
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.title

