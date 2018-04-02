# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-02 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0004_auto_20180402_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonname',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='common_name', to='species.Species'),
        ),
    ]
