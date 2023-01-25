from django.db import models


class Hall(models.Model):
    capacity = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=120)
    max_row = models.CharField(max_length=3)
    max_col = models.CharField(max_length=3)

    """trzeba przekminic jak zrobic walidacje kazdego siedzenia"""
