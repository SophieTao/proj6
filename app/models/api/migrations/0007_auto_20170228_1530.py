# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_cafe_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
