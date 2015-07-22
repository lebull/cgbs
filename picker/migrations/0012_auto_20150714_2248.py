# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0011_auto_20150714_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='sport',
        ),
        migrations.RemoveField(
            model_name='season',
            name='year',
        ),
        migrations.AddField(
            model_name='season',
            name='name',
            field=models.CharField(default='2015 NCAA Football', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 22, 48, 16, 854264, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
