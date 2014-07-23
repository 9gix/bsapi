# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_auto_20140720_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='user_book_request',
            new_name='loan_request',
        ),
        migrations.RemoveField(
            model_name='channelmessage',
            name='receiver',
        ),
    ]
