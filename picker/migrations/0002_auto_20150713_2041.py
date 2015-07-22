# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='complete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pick',
            name='winner',
            field=models.ForeignKey(default=0, to='picker.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='abreviation',
            field=models.CharField(default=b'????', max_length=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='away_score',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='home_score',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='kickoff_time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
