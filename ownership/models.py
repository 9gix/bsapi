from django.db import models

class Owner(models.Model):
    user = models.OneToOneField('auth.User')
    books = models.ManyToManyField('catalog.Book', through='OwnerBook')

    def __str__(self):
        return "Owner %s" % self.user

class OwnerBook(models.Model):
    owner = models.ForeignKey(Owner)
    book = models.ForeignKey('catalog.Book')

    def __str__(self):
        return "%s owns %s" % (self.owner, self.book)
