# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150904_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 9, 5, 3, 9, 22, 532228, tzinfo=utc), unique=True, verbose_name='slug'),
            preserve_default=False,
        ),
    ]
