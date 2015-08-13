# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0016_auto_20150813_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='yearcreditindex',
            new_name='weekcreditindex',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='yearcreditorder',
            new_name='weekcreditorder',
        ),
    ]
