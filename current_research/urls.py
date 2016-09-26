from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
        url(r'^index.html', research_index, name='view_research_index'),
    ]
