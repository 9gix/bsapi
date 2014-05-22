from django.db import models
from django.conf import settings

class Community(models.Model):
    name = models.CharField(max_length=40, unique=True)
    logo = models.ImageField(upload_to='community-logo', blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name
