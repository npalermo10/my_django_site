from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', teaching_index, name='view_teaching_index'),
    url(r'^(?P<slug>[^\.]+)/$', view_classroom, name='view_classroom'),
     ]
