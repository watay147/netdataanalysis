# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_company_stockno'),
    ]

    operations = [
        migrations.CreateModel(
            name='statics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companyname', models.CharField(max_length=80)),
                ('stadate', models.DateField()),
                ('possent', models.IntegerField()),
                ('negsent', models.IntegerField()),
                ('neusent', models.IntegerField()),
                ('creditindex', models.FloatField()),
                ('creditorder', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='attention',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='creditchange',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='creditindex',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='creditorder',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
