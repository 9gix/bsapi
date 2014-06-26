from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings

###this model contains the record of user's reputation

class Reputation(models.Model):
    value = models.IntegerField(default=10)
### initial total reputation amount set to be 10

    def increase(self, amount=1):
        value += amount
###function to increase user's reputation, default set to be 1

    def decrease(self, amount=1):
        value -= amount
###function to increase user's reputation, default set to be 1