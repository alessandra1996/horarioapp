from django.conf.urls import include,url
from django.contrib import admin
from apps.estudiantes.views import *
from django.conf.urls import patterns, url, include

urlpatterns = [
    url(r'^',include('apps.estudiantes.urls')),
    url(r'^admin/', include(admin.site.urls)),
]