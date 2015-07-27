# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='haha',
            field=models.CharField(default=datetime.datetime(2015, 7, 26, 8, 35, 39, 728000, tzinfo=utc), max_length=80),
            preserve_default=False,
        ),
    ]
