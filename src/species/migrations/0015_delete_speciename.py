# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-02 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0014_auto_20180402_1742'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SpecieName',
        ),
    ]