# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-02-12 20:04
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArrayFieldModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrays', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(choices=[(1, 'foo'), (2, 'bar')]), default=list, size=None)),
            ],
        ),
    ]
