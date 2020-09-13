from rest_framework import serializers
from .models import MovieDetail


class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieDetail
        fields = ('id', 'title', 'director', 'genre', 'rating', 'year', 'votes', 'kind')
        extra_kwargs = {
            'title':{'read_only':True}, 'director':{'read_only':True}, 'genre':{'read_only':True},
            'rating': {'read_only': True}, 'year':{'read_only':True}, 'votes':{'read_only':True},
            'kind':{'read_only':True}
        }