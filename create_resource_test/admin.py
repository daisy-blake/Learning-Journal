# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from create_resource_test.models import ResourceTest, Language, Framework, Database, Technology

# Register your models here.
admin.site.register(ResourceTest)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Database)
admin.site.register(Technology)
