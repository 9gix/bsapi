# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20140720_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='loan_request',
            field=models.OneToOneField(to='reservation.LoanRequest'),
        ),
    ]
