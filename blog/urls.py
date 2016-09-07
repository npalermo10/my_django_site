from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^index.html', blog_index, name='view_blog_index'),
    url(r'^view/(?P<slug>[^\.]+)/$', view_post, name='view_blog_post'),
    url(r'^category/(?P<slug>[^\.]+)/$', view_category, name='view_blog_category'),
    ]
