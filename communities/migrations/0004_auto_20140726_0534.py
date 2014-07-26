# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_auto_20140722_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True),
        ),
    ]
