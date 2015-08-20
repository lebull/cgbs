# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 17, 4, 52, 629403, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
