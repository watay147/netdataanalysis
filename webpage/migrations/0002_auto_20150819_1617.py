# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='mood',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='mood',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
