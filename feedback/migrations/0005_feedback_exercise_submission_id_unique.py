# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-18 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_feedback_submission_info'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together=set([('exercise', 'submission_id')]),
        ),
    ]
