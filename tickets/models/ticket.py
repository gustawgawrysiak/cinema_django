from django.db import models


class Ticket(models.Model):
    description = models.CharField(max_length=120)
    event_id = models.ForeignKey(to='theatre.Event', on_delete=models.PROTECT)
    seat_id = models.ForeignKey(to='theatre.Seat', on_delete=models.PROTECT)
