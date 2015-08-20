# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week', models.IntegerField()),
                ('kickoff_time', models.DateTimeField(null=True, blank=True)),
                ('complete', models.BooleanField(default=False)),
                ('away_score', models.IntegerField(null=True, blank=True)),
                ('home_score', models.IntegerField(null=True, blank=True)),
                ('location', models.CharField(max_length=b'50', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 8, 20, 16, 32, 15, 282633, tzinfo=utc))),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('game', models.ForeignKey(to='picker.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('active', models.BooleanField(default=False)),
                ('current_week', models.IntegerField(default=1)),
                ('users', models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('abreviation', models.CharField(default=b'????', max_length=4)),
                ('rank', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pick',
            name='winner',
            field=models.ForeignKey(to='picker.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(related_name='game_away_team', to='picker.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(related_name='game_home_team', to='picker.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(to='picker.Season'),
            preserve_default=True,
        ),
    ]
