# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-02 06:16
from __future__ import unicode_literals

import datetime
from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0005_auto_20180402_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='commonname',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2018, 4, 2, 14, 16, 10, 623079)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commonname',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True),
        ),
    ]
