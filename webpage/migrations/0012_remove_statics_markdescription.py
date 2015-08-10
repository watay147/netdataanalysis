# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0011_auto_20150807_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statics',
            name='markdescription',
        ),
    ]
