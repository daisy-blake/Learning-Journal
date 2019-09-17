# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from create_resource.models import LANGUAGE_CHOICES
from create_resource_test.models import Language, Framework, Database, Technology

# Create your views here.
def view_languages(request):
    choices = Language.objects.filter()


    return render(request, 'languages.html', {"choices": choices})

def update_language(request, pk):

    language = get_object_or_404(Language, pk=pk)
    if request.method == "POST":
        language.language = request.POST['language']
        language.save()
        return redirect('languages')
    else:
        value = language

    return render(request, 'update_language.html', {"value": value})


##########################################################


def view_frameworks(request):
    choices = Framework.objects.filter()


    return render(request, 'framework.html', {"choices": choices})

def update_framework(request, pk):

    framework = get_object_or_404(Framework, pk=pk)
    if request.method == "POST":
        framework.framework = request.POST['framework']
        framework.save()
        return redirect('frameworks')
    else:
        value = framework

    return render(request, 'update_framework.html', {"value": value})

###############################################################


def view_databases(request):
    choices = Database.objects.filter()


    return render(request, 'database.html', {"choices": choices})

def update_database(request, pk):

    database = get_object_or_404(Database, pk=pk)
    if request.method == "POST":
        database.database = request.POST['database']
        database.save()
        return redirect('databases')
    else:
        value = database

    return render(request, 'update_language.html', {"value": value})


#################################################


def view_technologys(request):
    choices = Technology.objects.filter()


    return render(request, 'technology.html', {"choices": choices})

def update_technology(request, pk):

    technology = get_object_or_404(Technology, pk=pk)
    if request.method == "POST":
        technology.technology = request.POST['technology']
        technology.save()
        return redirect('technologys')
    else:
        value = technology

    return render(request, 'update_language.html', {"value": value})





