# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='address',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
