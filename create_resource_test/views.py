# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from create_resource_test.forms import ResourceTestForm
from create_resource_test.models import ResourceTest, Language, Framework, Database, Technology

# Create your views here.
def create_resource_test(request):
    languages = Language.objects.all()
    frameworks = Framework.objects.all()
    databases = Database.objects.all()
    technologys = Technology.objects.all()

    variables = {
        'languages': languages,
        'frameworks': frameworks,
        'databases': databases,
        'technologys': technologys
    }

    if request.method == "POST":
        form = ResourceTestForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('home')



    return render(request, 'create_resource_test.html', variables)