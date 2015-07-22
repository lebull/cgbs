# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0010_auto_20150714_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pick',
            options={'get_latest_by': 'timestamp'},
        ),
        migrations.AddField(
            model_name='season',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 20, 41, 50, 159340, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
