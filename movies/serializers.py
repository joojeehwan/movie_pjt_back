from rest_framework import serializers
from .models import Movie, Actor, Genre


class MovieSerializer(serializers.ModelSerializer):
   
    # class ActorSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Actor
    #         fields = ('pk', 'name', )

    # class GenreSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Genre
    #         fields = ('pk', 'name')

    class Meta:
        model = Movie
        fields = '__all__'
        

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'