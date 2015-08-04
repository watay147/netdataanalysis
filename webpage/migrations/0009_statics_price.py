# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0008_auto_20150729_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='statics',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
