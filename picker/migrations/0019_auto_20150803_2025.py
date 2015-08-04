# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0018_auto_20150720_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pick',
            name='funny_looser_name',
        ),
        migrations.RemoveField(
            model_name='pick',
            name='funny_winner_name',
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 3, 20, 25, 9, 164720, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
