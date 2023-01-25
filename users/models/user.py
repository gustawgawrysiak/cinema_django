from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal


class User(AbstractUser):
    balance = models.DecimalField(default=Decimal(0))
    date_created = models.DateTimeField(auto_created=True)

    def set_balance(self, new_balance: Decimal) -> None:
        self.balance = new_balance

    def add_to_balance(self, price: Decimal) -> None:
        self.balance += price
        self.save()
