# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_events_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='hot',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='hot',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
