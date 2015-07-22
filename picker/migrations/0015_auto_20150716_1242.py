# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picker', '0014_auto_20150715_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(verbose_name=datetime.datetime(2015, 7, 16, 12, 42, 7, 12438, tzinfo=utc))),
                ('season', models.ForeignKey(to='picker.Season')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='pick',
            options={},
        ),
        migrations.AddField(
            model_name='season',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pick',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 12, 42, 7, 15331, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
