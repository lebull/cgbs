# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0007_auto_20150714_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='pick',
            name='funny_looser_name',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pick',
            name='funny_winner_name',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 14, 53, 0, 179579, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
