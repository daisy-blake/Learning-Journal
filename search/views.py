# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from create_resource.models import Resource


# Create your views here.
def search(request):
    print("B")
    if request.method == "GET":
        search = request.GET.get('search', False)
        resource = Resource.objects

        if resource.filter(name__icontains=search):
            all_resources = resource.filter(name__icontains=search).order_by("-created_date")

        elif resource.filter(link__icontains=search):
            all_resources = resource.filter(link__icontains=search).order_by("-created_date")

        elif resource.filter(language__icontains=search):
            all_resources = resource.filter(language__icontains=search).order_by("-created_date")

        elif resource.filter(framework__icontains=search):
            all_resources = resource.filter(framework__icontains=search).order_by("-created_date")

        elif resource.filter(database__icontains=search):
            all_resources = resource.filter(database__icontains=search).order_by("-created_date")

        elif resource.filter(technology__icontains=search):
            all_resources = resource.filter(technology__icontains=search).order_by("-created_date")

        else:
            all_resources = None
            messages.error(request, "No results found")

        return render(request, 'index.html', {"all_resources": all_resources})


def search_tech_type(request, tech_type):

    print("A")
    translation_table = dict.fromkeys(map(ord, '-'), ' ')
    tech_type = tech_type.title().translate(translation_table)
    print(tech_type)

    resource = Resource.objects

    if resource.filter(name__icontains=tech_type):
        all_resources = resource.filter(name__icontains=tech_type).order_by("-created_date")

    elif resource.filter(link__icontains=tech_type):
        all_resources = resource.filter(link__icontains=tech_type).order_by("-created_date")

    elif resource.filter(language__icontains=tech_type):
        all_resources = resource.filter(language__icontains=tech_type).order_by("-created_date")

    elif resource.filter(framework__icontains=tech_type):
        all_resources = resource.filter(framework__icontains=tech_type).order_by("-created_date")

    elif resource.filter(database__icontains=tech_type):
        all_resources = resource.filter(database__icontains=tech_type).order_by("-created_date")

    elif resource.filter(technology__icontains=tech_type):
        all_resources = resource.filter(technology__icontains=tech_type).order_by("-created_date")

    else:
        all_resources = None
        messages.error(request, "No results found")

    return render(request, 'index.html', {"all_resources": all_resources})
