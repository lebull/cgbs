# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0005_team_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='pick',
            name='latest',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
