# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newspost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='title',
            field=models.CharField(max_length=256, verbose_name='title'),
        ),
    ]
