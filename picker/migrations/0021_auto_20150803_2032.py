# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0020_auto_20150803_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 3, 20, 32, 10, 701291, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
