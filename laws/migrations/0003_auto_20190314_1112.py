# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-14 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0002_auto_20190312_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='objecttype',
            name='id_num',
            field=models.CharField(blank=True, default=None, max_length=8, null=True),
        ),
    ]
