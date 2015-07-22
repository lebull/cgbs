# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picker', '0015_auto_20150716_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_timestamp', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 13, 33, 38, 707013, tzinfo=utc))),
                ('action_timestamp', models.DateTimeField(default=None, null=True, blank=True)),
                ('accepted', models.NullBooleanField(default=None)),
                ('season', models.ForeignKey(to='picker.Season')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='seasonrequest',
            name='season',
        ),
        migrations.RemoveField(
            model_name='seasonrequest',
            name='user',
        ),
        migrations.DeleteModel(
            name='SeasonRequest',
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 13, 33, 38, 709150, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
