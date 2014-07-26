# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20140720_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='status',
            field=models.IntegerField(choices=[(0, 'Waiting for owner approval'), (1, 'Request approved'), (-1, 'Request unsuccessful')], default=0, max_length=1),
        ),
    ]
