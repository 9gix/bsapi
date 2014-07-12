# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.text import slugify

def create_unique_slug(apps, schema_editor):
    Category = apps.get_model('catalog', 'Category')

    for cat in Category.objects.all():
        cat.slug = slugify(cat.name)
        cat.save()
        if Category.objects.filter(slug=cat.slug).count() > 1:
            Category.objects.filter(slug=cat.slug)[0].delete()

def ignore_backward(*args, **kwargs):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_slug'),
    ]

    operations = [
        migrations.RunPython(create_unique_slug, ignore_backward),
    ]
