# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from create_resource.models import Resource
from create_resource_test.models import ResourceTest
from forms import ResourceTestUpdateForm

# Create your views here.
def home(request):
    all_resources = ResourceTest.objects.filter().order_by("-created_date")

    return render(request, 'index.html', {"all_resources": all_resources})

def update_resource(request, pk):
    resource = get_object_or_404(ResourceTest, pk=pk)
    if request.method == "POST":
        form = ResourceTestUpdateForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('home')


    else:
        form = ResourceTestUpdateForm(instance=resource)
        return render(request, 'update_resource.html', {'form': form})


def delete_resource(request, pk):
    resource = ResourceTest.objects.filter(pk=pk)
    resource.delete()
    return redirect('home')
