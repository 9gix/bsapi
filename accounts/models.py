from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.TextField()

    def __str__(self):
        return "%s's Profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

from communities.models import add_user_to_world_community
post_save.connect(add_user_to_world_community, sender=User)
