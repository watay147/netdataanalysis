# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0010_company_attentionreason'),
    ]

    operations = [
        migrations.AddField(
            model_name='statics',
            name='markdescription',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statics',
            name='shouldmark',
            field=models.BooleanField(default='nothing'),
            preserve_default=False,
        ),
    ]
