from django.db import models

class Owner(models.Model):
    user = models.OneToOneField('auth.User')
    books = models.ManyToManyField('catalog.Book', through='OwnerBook')

class OwnerBook(models.Model):
    owner = models.ForeignKey(Owner)
    book = models.ForeignKey('catalog.Book')
