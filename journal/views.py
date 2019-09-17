# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from create_resource.models import Resource
from create_resource_test.models import ResourceTest

# Create your views here.
def home(request):
    all_resources = ResourceTest.objects.filter().order_by("-created_date")
    return render(request, 'index.html', {"all_resources": all_resources})