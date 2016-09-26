from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^index.html', teaching_index, name='view_teacing_index'),
    ]
