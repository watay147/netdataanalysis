# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_auto_20150727_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stockno', models.CharField(max_length=6)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stockno', models.CharField(max_length=6)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
