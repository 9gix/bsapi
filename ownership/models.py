from django.db import models
from django.conf import settings

class UserBook(models.Model):
    """This model contains the information about the book owned by the owner
    such as book condition, etc.
    """
    book = models.ForeignKey('catalog.Book')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
            related_name='book_set')

    current_holder = models.ForeignKey(settings.AUTH_USER_MODEL,
            related_name='borrowed_books')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (owner: %s)" % (self.book, self.owner)

class BookPicture(models.Model):
    """This model contains the physical book photo, it is used to
    display the condition of the book."""
    user_book = models.ForeignKey('ownership.UserBook')
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
