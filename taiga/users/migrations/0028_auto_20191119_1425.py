# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-19 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20180610_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='public_key',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Public key'),
        ),
        migrations.AddField(
            model_name='user',
            name='threebot_name',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Threebot name'),
        ),
    ]
