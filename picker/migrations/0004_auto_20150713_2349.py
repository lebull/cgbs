# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0003_auto_20150713_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(default=1, to='picker.Season'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='season',
            name='sport',
            field=models.CharField(max_length=128, choices=[(b'NCAAF', b'NCAA Football')]),
            preserve_default=True,
        ),
    ]
