# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-02 07:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0007_auto_20180402_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classname',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='family',
            options={'verbose_name': 'Family', 'verbose_name_plural': 'Families'},
        ),
        migrations.AlterModelOptions(
            name='genus',
            options={'verbose_name': 'Genus', 'verbose_name_plural': 'Genera'},
        ),
        migrations.AlterModelOptions(
            name='kingdom',
            options={'verbose_name': 'Kingdom', 'verbose_name_plural': 'Kingdoms'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='phylum',
            options={'verbose_name': 'Phylum', 'verbose_name_plural': 'Phyla'},
        ),
    ]
