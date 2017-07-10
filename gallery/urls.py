from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
        url(r'^index.html', gallery_index, name='view_gallery_index'),
        url(r'^(?P<slug>[^\.]+)/$', view_album, name='view_album'),
        ]
