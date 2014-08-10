# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0001_initial'),
        ('communities', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='reputation',
            name='membership',
            field=models.OneToOneField(default=1, to_field='id', to='communities.Membership'),
            preserve_default=False,
        ),
    ]
