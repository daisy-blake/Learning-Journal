# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from create_resource_test.forms import ResourceTestForm
from create_resource_test.models import ResourceTest, Language, Framework, Database, Technology

# Create your views here.
def create_resource_test(request):
    # languages = Language.objects.all()
    # frameworks = Framework.objects.all()
    # databases = Database.objects.all()
    # technologys = Technology.objects.all()
    #
    # variables = {
    #     'languages': languages,
    #     'frameworks': frameworks,
    #     'databases': databases,
    #     'technologys': technologys
    # }

    if request.method == "POST":
        form = ResourceTestForm(request.POST, request.FILES)
        print(form)
        language = request.POST.get('language')
        framework = request.POST.get('framework')
        database = request.POST.get('database')
        technology = request.POST.get('technology')

        if form.is_valid():
            print("B")
            resource = form.save()

        return redirect('home')
    else:
        form = ResourceTestForm

    return render(request, 'create_resource_test.html', {"form": form})