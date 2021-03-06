# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-02 05:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='CommonName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Phylum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SpecieName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sciname_author', models.CharField(max_length=80)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['genus', 'speciename'])),
                ('updated', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('classname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='species.ClassName')),
                ('common_title', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='local_name', to='species.CommonName')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='species.Family')),
                ('genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='species.Genus')),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='species.Kingdom')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='species.Order')),
                ('phylum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='species.Phylum')),
                ('speciename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='species.SpecieName')),
            ],
        ),
    ]
