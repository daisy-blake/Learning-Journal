from django.conf.urls import url
from tech_types.views import view_languages, update_language, view_frameworks, update_framework, view_databases, update_database, view_technologys, update_technology, create_language, create_framework, create_database, create_technology, delete_language, delete_framework, delete_technology, delete_database

urlpatterns = [
    url(r'languages/$', view_languages, name="languages"),
    url(r'languages/(?P<pk>\d+)/$', update_language, name="update_language"),
    url(r'languages/new/$', create_language, name="create_language"),
    url(r'languages/(?P<pk>\d+)/remove/$', delete_language, name="delete_language"),
    url(r'frameworks/$', view_frameworks, name="frameworks"),
    url(r'frameworks/(?P<pk>\d+)/$', update_framework, name="update_framework"),
    url(r'frameworks/new/$', create_framework, name="create_framework"),
    url(r'frameworks/(?P<pk>\d+)/remove/$', delete_framework, name="delete_framework"),
    url(r'databases/$', view_databases, name="databases"),
    url(r'databases/(?P<pk>\d+)/$', update_database, name="update_database"),
    url(r'databases/new/$', create_database, name="create_database"),
    url(r'databases/(?P<pk>\d+)/remove/$', delete_database, name="delete_database"),
    url(r'technologys/$', view_technologys, name="technologys"),
    url(r'technologys/(?P<pk>\d+)/$', update_technology, name="update_technology"),
    url(r'technologys/new/$', create_technology, name="create_technology"),
    url(r'technologys/(?P<pk>\d+)/remove/$', delete_technology, name="delete_technology"),


]
