# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-05 04:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0021_auto_20180405_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='commonname',
            name='scientific_name',
            field=models.CharField(blank=True, help_text='automatically saved', max_length=120),
        ),
        migrations.AlterField(
            model_name='classname',
            name='group_as',
            field=models.ForeignKey(blank=True, help_text='term used by many to easily identify this species e.g Aves is to birds, ', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classname', to='species.Category', verbose_name='Categorize as'),
        ),
    ]