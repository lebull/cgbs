# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0004_auto_20150713_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='rank',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
