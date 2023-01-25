from django.db import models
from ..utils.choices import FilmCategory


class Film(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    length = models.IntegerField()
    category = models.CharField(choices=FilmCategory.choices, default=None, max_length=10)
