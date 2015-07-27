# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_remove_company_haha'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='stockno',
            field=models.CharField(default='000415', max_length=6),
            preserve_default=False,
        ),
    ]
