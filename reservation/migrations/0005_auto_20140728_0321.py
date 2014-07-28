# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def update_int_to_str_status(apps, schema_editor):
    LoanRequest = apps.get_model('reservation', 'LoanRequest')
    for lr in LoanRequest.objects.all():
        lr.status = {
            '1': 'approved',
            '0': 'pending',
            '-1': 'rejected',
        }[lr.status]
        lr.save()

def update_str_to_int_status(apps, schema_editor):
    LoanRequest = apps.get_model('reservation', 'LoanRequest')
    for lr in LoanRequest.objects.all():
        lr.status = {
                'approved': '1',
                'pending': '0',
                'rejected': '-1',
        }[lr.status]
        lr.save()

class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20140728_0320'),
    ]

    operations = [
        migrations.RunPython(
            update_int_to_str_status,
            update_str_to_int_status),
    ]
