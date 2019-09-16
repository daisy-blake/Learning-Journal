from django.conf.urls import url
from views import create_resource

urlpatterns = [
    url(r'^$', create_resource, name="create_resource")
]