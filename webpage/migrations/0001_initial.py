# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('intro', models.TextField()),
                ('finance', models.TextField()),
                ('ope', models.TextField()),
                ('stockno', models.CharField(max_length=6)),
                ('creditindex', models.FloatField()),
                ('creditorder', models.IntegerField()),
                ('creditchange', models.IntegerField()),
                ('attention', models.BooleanField()),
                ('attentionreason', models.CharField(max_length=1000)),
                ('weekcreditindex', models.FloatField()),
                ('weekcreditorder', models.IntegerField()),
                ('moncreditindex', models.FloatField()),
                ('moncreditorder', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stockno', models.CharField(max_length=6)),
                ('comname', models.CharField(max_length=80)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('click', models.IntegerField()),
                ('reply', models.IntegerField()),
                ('source', models.CharField(max_length=40)),
                ('hot', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stockno', models.CharField(max_length=6)),
                ('comname', models.CharField(max_length=80)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('click', models.IntegerField()),
                ('reply', models.IntegerField()),
                ('source', models.CharField(max_length=40)),
                ('hot', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='statics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stockno', models.CharField(max_length=6)),
                ('stadate', models.DateField()),
                ('possent', models.IntegerField()),
                ('negsent', models.IntegerField()),
                ('neusent', models.IntegerField()),
                ('creditindex', models.FloatField()),
                ('creditorder', models.IntegerField()),
                ('price', models.FloatField()),
                ('shouldmark', models.BooleanField()),
            ],
        ),
    ]
