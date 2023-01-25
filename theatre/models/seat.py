from django.db import models
from ..utils.choices import SeatCategory


class Seat(models.Model):
    hall_id = models.ForeignKey('theatre.Hall', on_delete=models.PROTECT)
    seat_category = models.CharField(choices=SeatCategory.choices, default=SeatCategory.NORMAL, max_length=12)
    # taken = models.BooleanField(default=False) # may cause problems, need to update user_id and flag each time
    # user_id = models.ForeignKey('users.User', on_delete=models.PROTECT)
    # no need to assign user and bool, while multiple events on 1 hall it will cause problems
    place = models.CharField(max_length=3) # validate X and Y offset on create, mbe row and col separately
    description = models.CharField(null=True, max_length=120)
