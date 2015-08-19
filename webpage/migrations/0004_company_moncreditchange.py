# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_company_weekcreditchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='moncreditchange',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
