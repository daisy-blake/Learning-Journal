# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

LANGUAGE_CHOICES = (
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('Ruby', 'Ruby'),
        ('AdibsLanguage', 'AdibsLanguage')
)

FRAMEWORK_CHOICES = (
    ('Django', 'Django'),
    ('Flask', 'Flask'),
    ('Spring boot', 'Spring boot')
)

DATABASE_CHOICES = (
    ('MySQL', 'MySQL'),
    ('PostgreSQL', 'PostgreSQL'),
    ('MongoDB', 'MongoDB')
)

TECHNOLOGY_CHOICES = (
    ('AWS', 'AWS'),
    ('Programming', 'Programming'),
    ('Git', 'Git'),
    ('Web', 'Web'),
    ('Machine Learning', 'Machine Learning')
)

# Create your models here.
class Resource(models.Model):

    name = models.CharField(max_length=400)
    link = models.CharField(max_length=1000, blank=True, null=True)
    attachment = models.FileField(upload_to='documents', blank=True, null=True)
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, blank=True, null=True)
    framework = models.CharField(max_length=100, choices=FRAMEWORK_CHOICES, blank=True, null=True)
    database = models.CharField(max_length=100, choices=DATABASE_CHOICES, blank=True, null=True)
    technology = models.CharField(max_length=100, choices=TECHNOLOGY_CHOICES, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    # published_date = models.DateTimeField(blank=True, null=True, default=timezone.now())

    def __str__(self):
        return self.name


# UPDATE mysql.user SET Password=PASSWORD('Password') WHERE User='root';
# SET PASSWORD FOR 'root' = PASSWORD('Password');
# update user set authentication_string=password('Password') where user='root';
