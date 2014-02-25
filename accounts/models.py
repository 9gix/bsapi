from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User)
    address = models.TextField()

def create_user_detail(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.get_or_create(user=instance)

post_save.connect(create_user_detail, sender=User)
