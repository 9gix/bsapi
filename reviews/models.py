from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Review(models.Model):

    # Generic Review
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # User as Reviewer
    reviewer = models.ForeignKey('auth.User')

    # Review content
    headline = models.CharField(max_length=100)
    content = models.TextField()

    rating = models.FloatField(
            validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
