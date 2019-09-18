# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from create_resource.models import LANGUAGE_CHOICES
from create_resource_test.models import Language, Framework, Database, Technology
from forms import NewLanguageForm, NewDatabaseForm, NewFrameworkForm, NewTechnologyForm

# Create your views here.
def view_languages(request):
    choices = Language.objects.filter()

    print(choices)

    return render(request, 'languages.html', {"choices": choices})

def update_language(request, pk):
    print("Firing")
    language = get_object_or_404(Language, pk=pk)
    if request.method == "POST":
        language.language = request.POST['language']
        language.save()
        return redirect('languages')
    else:
        value = language

    return render(request, 'update_language.html', {"value": value})

def create_language(request):
    print("LANGAUGE FIRING")
    if request.method == "POST":
        form = NewLanguageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('languages')
    else:
        return render(request, 'create_language.html')

def delete_language(request, pk):
    language = get_object_or_404(Language, pk=pk)
    language.delete()
    return redirect('languages')



##########################################################


def view_frameworks(request):
    choices = Framework.objects.filter()
    return render(request, 'frameworks.html', {"choices": choices})

def update_framework(request, pk):

    framework = get_object_or_404(Framework, pk=pk)
    if request.method == "POST":
        framework.framework = request.POST['framework']
        framework.save()
        return redirect('frameworks')
    else:
        value = framework
        print(value)

    return render(request, 'update_framework.html', {"value": value})

def create_framework(request):
    print("TESTING")
    if request.method == "POST":
        form = NewFrameworkForm(request.POST)
        print(form)
        if form.is_valid():
            print("form is valid")
            form.save()
        return redirect('frameworks')
    else:
        return render(request, 'create_framework.html')

def delete_framework(request, pk):
    framework = get_object_or_404(Framework, pk=pk)
    framework.delete()
    return redirect('frameworks')

###############################################################


def view_databases(request):
    choices = Database.objects.filter()


    return render(request, 'databases.html', {"choices": choices})

def update_database(request, pk):

    database = get_object_or_404(Database, pk=pk)
    if request.method == "POST":
        database.database = request.POST['database']
        database.save()
        return redirect('databases')
    else:
        value = database

    return render(request, 'update_database.html', {"value": value})

def create_database(request):
    if request.method == "POST":
        form = NewDatabaseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('databases')
    else:
        return render(request, 'create_database.html')

def delete_database(request, pk):
    database = get_object_or_404(Database, pk=pk)
    database.delete()
    return redirect('databases')


#################################################


def view_technologys(request):
    choices = Technology.objects.filter()


    return render(request, 'technologys.html', {"choices": choices})

def update_technology(request, pk):

    technology = get_object_or_404(Technology, pk=pk)
    if request.method == "POST":
        technology.technology = request.POST['technology']
        technology.save()
        return redirect('technologys')
    else:
        value = technology

    return render(request, 'update_technology.html', {"value": value})

def create_technology(request):
    if request.method == "POST":
        form = NewTechnologyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('technologys')
    else:
        return render(request, 'create_technology.html')

def delete_technology(request, pk):
    technology = get_object_or_404(Technology, pk=pk)
    technology.delete()
    return redirect('technologys')





