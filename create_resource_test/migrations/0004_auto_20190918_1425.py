# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-18 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create_resource_test', '0003_resourcetest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcetest',
            name='database',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='create_resource_test.Database'),
        ),
        migrations.AlterField(
            model_name='resourcetest',
            name='framework',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='create_resource_test.Framework'),
        ),
        migrations.AlterField(
            model_name='resourcetest',
            name='language',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='create_resource_test.Language'),
        ),
        migrations.AlterField(
            model_name='resourcetest',
            name='technology',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='create_resource_test.Technology'),
        ),
    ]
