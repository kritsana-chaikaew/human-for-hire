# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 08:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_auto_20170929_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.AddField(
            model_name='product',
            name='init_date',
            field=models.DateField(default=datetime.date(2017, 9, 30)),
        ),
    ]
