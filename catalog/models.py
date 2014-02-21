from django.db import models
from catalog.isbn import checkI10, checkI13
from django.core.exceptions import ValidationError


def isbn10_validator(isbn):
    if not checkI10(isbn):
        raise ValidationError(u'%s is not a valid ISBN-10' % isbn)

def isbn13_validator(isbn):
    if not checkI13(isbn):
        raise ValidationError(u'%s is not a valid ISBN-13' % isbn)

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    isbn10 = models.CharField(
            max_length=10, unique=True,
            validators=[isbn10_validator],
            help_text="Enter the unique ISBN-10",
            blank=True, null=True)

    isbn13 = models.CharField(
            max_length=13, unique=True,
            validators=[isbn13_validator],
            help_text="Enter the unique ISBN-13",
            blank=True, null=True)

    description = models.TextField(blank=True)

    url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


