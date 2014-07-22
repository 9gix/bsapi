# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=datetime.date(2014, 7, 22), editable=False, unique=True),
            preserve_default=False,
        ),
    ]
