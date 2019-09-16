from django.conf.urls import url#

from search.views import search, search_tech_type

urlpatterns = [
    url(r'^$', search, name='search'),
    url(r'^(?P<tech_type>[-\w\d]+)/$', search_tech_type, name='search_tech_type')
]