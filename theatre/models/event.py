from django.db import models
from ..utils.choices import EventCategory


class Event(models.Model):
    hall_id = models.ForeignKey(to='theatre.Hall',
                                on_delete=models.PROTECT)
    film_id = models.ForeignKey(to='theatre.Film',
                                on_delete=models.PROTECT)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    category = models.CharField(choices=EventCategory.choices,
                                default=EventCategory.FILM,
                                max_length=10)
