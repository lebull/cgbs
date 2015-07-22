# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0002_auto_20150713_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sport', models.CharField(max_length=128)),
                ('year', models.IntegerField(default=2015)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='game',
            name='kickoff_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
