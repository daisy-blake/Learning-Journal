# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-10 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_resource', '0005_resource_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
