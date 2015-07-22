# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0006_pick_latest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pick',
            name='latest',
        ),
        migrations.AddField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 14, 46, 11, 799435, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
