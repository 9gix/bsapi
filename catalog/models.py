from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from catalog.isbn import checkI10, checkI13

from autoslug import AutoSlugField
import pyisbn

def isbn_validator(isbn):
    if not pyisbn.validate(isbn):
        raise ValidationError(u'%s is not a valid ISBN-13' % isbn)

class BookQuerySet(models.query.QuerySet):
    pass

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True,
            populate_from=lambda obj: "%s-%s" % (obj.isbn13, obj.title))

    isbn13 = models.CharField(
            max_length=13, unique=True,
            validators=[MinLengthValidator(13), isbn_validator],
            help_text="Enter the unique ISBN-13",
            blank=True, null=True)

    description = models.TextField(blank=True)

    url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = BookQuerySet.as_manager()
