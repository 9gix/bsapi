from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save

from autoslug import AutoSlugField
import pyisbn

from catalog.isbn import checkI10, checkI13

def isbn_validator(isbn):
    if not pyisbn.validate(isbn):
        raise ValidationError(u'%s is not a valid ISBN-13' % isbn)

class BookGeneric(models.Model):
    """This model is a generic book attribute regardless of the owner
    such as isbn, title, author, version, publisher, etc. as needed 
    """

    isbn13 = models.CharField(
            max_length=13, unique=True,
            validators=[MinLengthValidator(13), isbn_validator],
            help_text="Enter the unique ISBN-13",
            blank=True, null=True)

    def __str__(self):
        return self.isbn13
