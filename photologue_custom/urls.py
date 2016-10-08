from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'gallery', gallery_list, name='view_gallery_index'),
    ]
