# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-07-06 11:11
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0002_auto_20170118_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='form_i18n',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]