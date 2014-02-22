from django.db import models

class UserBook(models.Model):
    owner = models.ForeignKey('auth.User')
    book = models.ForeignKey('catalog.Book')
