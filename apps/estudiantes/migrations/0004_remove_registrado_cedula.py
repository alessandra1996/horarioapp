# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-06 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0003_auto_20161006_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrado',
            name='cedula',
        ),
    ]