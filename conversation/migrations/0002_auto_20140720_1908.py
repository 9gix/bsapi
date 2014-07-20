# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
        ('reservation', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='appointment_at',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='channel',
            name='user_book_request',
            field=models.OneToOneField(to='reservation.UserBookRequest', default=1),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name='channelmessage',
            old_name='conversation',
            new_name='channel',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='borrower',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='reservation_status',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='user_book',
        ),
    ]
