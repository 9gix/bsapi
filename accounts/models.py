from django.db import models

class UserDetail(models.Model):
    user = models.OneToOneField('auth.User')
    address = models.TextField()
