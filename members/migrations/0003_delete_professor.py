# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 21:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20161127_0153'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Professor',
        ),
    ]