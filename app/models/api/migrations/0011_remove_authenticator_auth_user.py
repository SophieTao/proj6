# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-19 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_authenticator_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authenticator',
            name='auth_user',
        ),
    ]
