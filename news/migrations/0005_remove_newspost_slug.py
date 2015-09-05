# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newspost_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspost',
            name='slug',
        ),
    ]
