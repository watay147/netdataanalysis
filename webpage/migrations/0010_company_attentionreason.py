# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0009_statics_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='attentionreason',
            field=models.CharField(default='nothing', max_length=1000),
            preserve_default=False,
        ),
    ]
