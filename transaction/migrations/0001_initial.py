# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ownership', '__first__'),
        ('communities', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('transaction_date', models.DateField(auto_now_add=True)),
                ('transaction_status', models.SmallIntegerField(default=1, choices=[(1, 'On Loan'), (0, 'Available'), (-1, 'Lost')])),
                ('book', models.ForeignKey(to='ownership.UserBook')),
                ('borrow_membership', models.ForeignKey(to='communities.Membership')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
