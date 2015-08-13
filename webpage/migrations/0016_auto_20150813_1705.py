# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0015_auto_20150813_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='moncreditindex',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='moncreditorder',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='yearcreditindex',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='yearcreditorder',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
