# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-11 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0023_remove_commonname_scientific_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciesimage',
            name='species',
            field=models.ForeignKey(help_text='Add your species image(s) here', on_delete=django.db.models.deletion.CASCADE, related_name='specie_image', to='species.Species'),
        ),
    ]