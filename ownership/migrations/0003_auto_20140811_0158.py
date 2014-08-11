# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ownership', '0002_auto_20140811_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
