from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save

from autoslug import AutoSlugField
import pyisbn

from catalog.isbn import checkI10, checkI13

def isbn_validator(isbn):
    try:
        pyisbn.validate(isbn)
    except pyisbn.IsbnError as err:
        raise ValidationError(err.message)

class Author(models.Model):
    name = models.CharField(max_length=45, help_text="Full Name")

    @property
    def first_name(self):
        return self.name.split()[:1]

    @property
    def given_name(self):
        return self.name.split()[:-1] or self.name

    @property
    def last_name(self):
        return "".join(self.name.split()[-1:])

    @property
    def apa_name(self):
        """APA style name for citation or reference
        e.g. Ned Eddard Stark into Stark, N. E."""
        if len(self.name.split()) <= 1:
            return self.name

        initial = reduce(
            lambda initial, name: "{}{}. ".format(initial, name[0]), 
            self.name.split()[:-1], "").strip()
        return "{}, {}".format(self.last_name, initial)

    def __str__(self):
        return self.apa_name

class Publisher(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=45)

class BookProfile(models.Model):
    """This model is a generic book attribute regardless of the owner
    such as isbn, title, author, version, publisher, etc. as needed 
    """

    isbn13 = models.CharField(
            max_length=13, unique=True,
            validators=[MinLengthValidator(13), isbn_validator],
            help_text="Enter the unique ISBN-13",
            blank=True, null=True)

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255, blank=True)

    thumbnail = models.ImageField(blank=True)

    publisher = models.ForeignKey('catalog.Publisher')
    authors = models.ManyToManyField('catalog.Author')
    categories = models.ManyToManyField('catalog.Category')

    published_on = models.DateField()

    owners = models.ManyToManyField('auth.User', through='ownership.Book', 
            related_name='bookprofiles')

    def __str__(self):
        return "{}, {}".format(self.title, self.isbn13)
