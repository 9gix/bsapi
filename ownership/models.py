from django.db import models

class Book(models.Model):
    """This model contains the information about the book owned by the owner
    such as book condition, etc.
    """
    book_profile = models.ForeignKey('catalog.BookProfile')
    owner = models.ForeignKey('auth.User')

    class Meta:
        unique_together = ('book_profile', 'owner')

    def __str__(self):
        return "%s (owner: %s)" % (self.book_profile, self.owner)

class BookPicture(models.Model):
    """This model contains the physical book photo, it is used to
    display the condition of the book."""
    book = models.ForeignKey('ownership.Book')
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
