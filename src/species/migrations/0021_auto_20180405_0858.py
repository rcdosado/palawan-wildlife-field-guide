# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-05 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0020_auto_20180405_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='classname',
            field=models.ForeignKey(help_text='The full scientific name of the class in which the taxon is classified.', on_delete=django.db.models.deletion.CASCADE, related_name='class_category', to='species.ClassName', verbose_name='class'),
        ),
    ]
