# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-25 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20160925_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='year',
            field=models.DateTimeField(),
        ),
    ]