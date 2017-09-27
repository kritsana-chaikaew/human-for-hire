# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20170926_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller_username',
            field=models.CharField(default='seller_username', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
