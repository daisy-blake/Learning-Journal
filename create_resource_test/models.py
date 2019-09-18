# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Language(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language

class Framework(models.Model):
    framework = models.CharField(max_length=100)

    def __str__(self):
        return self.framework

class Database(models.Model):
    database = models.CharField(max_length=100)

    def __str__(self):
        return self.database

class Technology(models.Model):
    technology = models.CharField(max_length=100)

    def __str__(self):
        return self.technology

class ResourceTest(models.Model):
    name = models.CharField(max_length=400)
    link = models.CharField(max_length=1000, blank=True, null=True)
    attachment = models.FileField(upload_to='documents', blank=True, null=True)
    language = models.ForeignKey(Language, default=None)
    framework = models.ForeignKey(Framework, default=None)
    database = models.ForeignKey(Database, default=None)
    technology = models.ForeignKey(Technology, default=None)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    # published_date = models.DateTimeField(blank=True, null=True, default=timezone.now())

    def __str__(self):
        return self.name