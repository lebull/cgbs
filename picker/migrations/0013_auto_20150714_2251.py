# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0012_auto_20150714_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='current_week',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 22, 51, 26, 275907, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
