from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^index.html', publication_index, name='view_publication_index'),
    ]
