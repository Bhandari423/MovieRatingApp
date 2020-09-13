from django.db import models


class MovieDetail(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    year = models.IntegerField()
    votes = models.IntegerField()
    kind = models.CharField(max_length=250)
