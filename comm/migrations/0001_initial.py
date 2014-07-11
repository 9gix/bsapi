# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ownership', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('reservation_status', models.SmallIntegerField(default=0, choices=[(0, 'Waiting for approval'), (1, 'Request approved'), (-1, 'Request unsuccessful')])),
                ('borrower', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user_book', models.ForeignKey(to='ownership.UserBook')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConversationMessage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('conversation', models.ForeignKey(to='comm.Conversation')),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
