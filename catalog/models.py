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

class BookQuerySet(models.query.QuerySet):
    pass

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)

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
    date = models.DateField(blank=True, null=True)
    authors = models.ManyToManyField(Author, blank=True)
    publishers = models.ManyToManyField(Publisher, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BookQuerySet.as_manager()

def sync_book_data(sender, instance, created, **kwargs):

    if instance.isbn13:
        from catalog.tasks import fetch_and_update_book_info_task
        fetch_and_update_book_info_task.delay(instance.isbn13)


post_save.connect(sync_book_data, sender=Book)
