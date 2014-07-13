# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20140713_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, unique=True, help_text='Full Name'),
        ),
    ]
