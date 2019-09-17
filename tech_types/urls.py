from django.conf.urls import url
from tech_types.views import view_languages, update_language, view_frameworks, update_framework, view_databases, update_database, view_technologys, update_technology

urlpatterns = [
    url(r'languages/', view_languages, name="languages"),
    url(r'(?P<pk>\d+)/$', update_language, name="update_language"),
    url(r'frameworks/', view_frameworks, name="frameworks"),
    url(r'(?P<pk>\d+)/$', update_framework, name="update_framework"),
    url(r'databases/', view_databases, name="databases"),
    url(r'(?P<pk>\d+)/$', update_database, name="update_database"),
    url(r'technologys/', view_technologys, name="technologys"),
    url(r'(?P<pk>\d+)/$', update_technology, name="update_technology"),



]
