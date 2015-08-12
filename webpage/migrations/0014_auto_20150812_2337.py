# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0013_auto_20150812_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='comname',
            field=models.CharField(default='\u6e24\u6d77\u79df\u8d41', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='comname',
            field=models.CharField(default='\u6e24\u6d77\u79df\u8d41', max_length=80),
            preserve_default=False,
        ),
    ]
