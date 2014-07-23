# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def create_world_community(apps, schema_editor):
    Community = apps.get_model('communities', 'Community')
    Community.objects.create(name='World', slug='world')

def delete_world_community(apps, schema_editor):
    Community = apps.get_model('communities', 'Community')
    Community.objects.filter(slug='world').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_community_slug'),
    ]

    operations = [
        migrations.RunPython(create_world_community, delete_world_community),
    ]
