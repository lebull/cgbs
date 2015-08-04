# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0019_auto_20150803_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 3, 20, 29, 12, 91155, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
