from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique = True)
    posted = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('gallery:view_album', kwargs= {'slug': self.slug })

class Photo(models.Model):
    title = models.CharField(max_length = 100, blank=True)
    slug = models.ForeignKey("gallery.Album")
    date = models.DateField(blank = True)
    img = models.ImageField()
