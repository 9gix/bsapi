# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_remove_transaction_transaction_status'),
        ('reservation', '0002_auto_20140720_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='loan_request',
            field=models.OneToOneField(to='reservation.LoanRequest', null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='book',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='borrow_membership',
        ),
    ]
