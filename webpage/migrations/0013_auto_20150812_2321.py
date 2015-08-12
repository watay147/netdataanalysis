# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0012_remove_statics_markdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='click',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='reply',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='source',
            field=models.CharField(default='\u4e1c\u65b9\u8d22\u5bcc\u7f51\u80a1\u5427', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='click',
            field=models.IntegerField(default=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='reply',
            field=models.IntegerField(default=214),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.CharField(default='\u4e1c\u65b9\u8d22\u5bcc\u7f51\u80a1\u5427', max_length=40),
            preserve_default=False,
        ),
    ]
