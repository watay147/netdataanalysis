# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_auto_20150727_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statics',
            name='companyname',
        ),
        migrations.AddField(
            model_name='statics',
            name='stockno',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
    ]
