# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-02 10:21
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0016_auto_20180402_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['genus', 'specie'], verbose_name='Name'),
        ),
    ]
