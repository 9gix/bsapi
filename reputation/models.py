from django.db import models


class Reputation(models.Model):
    """this model contains the record of user's reputation"""

    value = models.IntegerField(default=0)

    def increase(self, amount=1):
        self.value += amount

    def decrease(self, amount=1):
        self.value -= amount
