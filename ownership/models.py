from django.db import models

class Book(models.Model):
    """This model contains the information about the book owned by the owner
    such as book condition, etc.
    """
    book_generic = models.ForeignKey('catalog.BookGeneric')
    owner = models.ForeignKey('auth.User')

    def __str__(self):
        return "%s owns %s" % (self.owner, self.book_generic)

class BookPicture(models.Model):
    book = models.ForeignKey('ownership.Book')
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
