# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import colorful.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0017_auto_20150716_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinrequest',
            name='season',
        ),
        migrations.RemoveField(
            model_name='joinrequest',
            name='user',
        ),
        migrations.DeleteModel(
            name='JoinRequest',
        ),
        migrations.RemoveField(
            model_name='season',
            name='owner',
        ),
        migrations.AddField(
            model_name='team',
            name='primary_color',
            field=colorful.fields.RGBColorField(default=(0, 0, 0)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 20, 14, 18, 33, 664046, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
