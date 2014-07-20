# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
        ('communities', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='borrower_membership',
            field=models.ForeignKey(default=1, to='communities.Membership'),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='user_book',
            new_name='owner_book',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='borrower',
        ),
    ]
