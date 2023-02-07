from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    length = models.IntegerField()

