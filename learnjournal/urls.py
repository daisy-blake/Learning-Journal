"""learnjournal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from journal.views import home
from create_resource import urls as create_resource_urls
from create_resource_test import urls as create_resource_test_urls
from search import urls as search_urls
from tech_types import urls as tech_types_urls



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^create-resource/', include(create_resource_urls)),
    url(r'^create-resource_test/', include(create_resource_test_urls)),
    url(r'^search/', include(search_urls)),
    url(r'tech-types/', include(tech_types_urls))
]
