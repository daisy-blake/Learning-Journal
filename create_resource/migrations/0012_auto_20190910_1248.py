# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-10 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_resource', '0011_resource_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='resource',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
