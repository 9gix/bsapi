from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings


class Reputation(models.Model):
    """this model contains the record of user's reputation"""

    value = models.IntegerField(default=0)

    def increase(self, amount=1):
        self.value += amount

    def decrease(self, amount=1):
        self.value -= amount
