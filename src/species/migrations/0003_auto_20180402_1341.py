# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-02 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0002_auto_20180402_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classname',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='genus',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kingdom',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='phylum',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speciename',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
