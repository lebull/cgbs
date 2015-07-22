# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picker', '0016_auto_20150716_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='owner',
            field=models.ForeignKey(related_name='owner', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='joinrequest',
            name='created_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 15, 16, 25, 357353, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 15, 16, 25, 359537, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='season',
            name='users',
            field=models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
