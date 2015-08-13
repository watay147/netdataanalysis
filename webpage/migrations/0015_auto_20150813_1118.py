# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0014_auto_20150812_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
        migrations.AddField(
            model_name='company',
            name='finance',
            field=models.TextField(default='xxx'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='intro',
            field=models.TextField(default='xxxxxxx'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='ope',
            field=models.TextField(default='xxxxxxxxxxx\nlllll'),
            preserve_default=False,
        ),
    ]
