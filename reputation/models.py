from django.db import models
from django.db.models.signals import post_save


class Reputation(models.Model):
    """this model contains the record of user's reputation"""

    membership = models.OneToOneField('communities.Membership')
    value = models.IntegerField(default=0)

    def increase(self, amount=1):
        self.value += amount

    def decrease(self, amount=1):
        self.value -= amount

def create_membership_reputation(sender, instance, created, **kwargs):
    if created:
        Reputation.objects.get_or_create(membership=instance)

post_save.connect(create_membership_reputation, sender='communities.Membership')
