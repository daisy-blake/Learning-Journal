from django.conf.urls import url
from create_resource_test.views import create_resource_test

urlpatterns = [
    url(r'^$', create_resource_test, name="create_resource_test")
]