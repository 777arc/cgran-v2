# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-29 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ootlist', '0007_auto_20170921_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='outoftreemodule',
            name='body_text',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
