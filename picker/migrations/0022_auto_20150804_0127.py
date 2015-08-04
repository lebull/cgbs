# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0021_auto_20150803_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.CharField(max_length=b'50', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 1, 27, 37, 692989, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
