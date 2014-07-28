# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20140726_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='status',
            field=models.CharField(max_length=8, default='pending', choices=[('pending', 'Waiting for owner approval'), ('approved', 'Loan Request approved'), ('rejected', 'Loan Request rejected')]),
        ),
    ]
