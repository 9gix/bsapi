from django.db import models

class Book(models.Model):
    """This model contains the information about the book owned by the owner
    such as book condition, etc.
    """
    book_generic = models.ForeignKey('catalog.BookGeneric')
    owner = models.ForeignKey('auth.User')

    class Meta:
        unique_together = ('book_generic', 'owner')

    def __str__(self):
        return "%s (owner: %s)" % (self.book_generic, self.owner)

class BookPicture(models.Model):
    book = models.ForeignKey('ownership.Book')
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
