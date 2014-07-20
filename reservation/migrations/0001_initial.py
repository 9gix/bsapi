# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ownership', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('status', models.IntegerField(max_length=1, choices=[(0, 'Waiting for owner approval'), (1, 'Request approved'), (-1, 'Request unsuccessful')])),
                ('borrower', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user_book', models.ForeignKey(to='ownership.UserBook')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
