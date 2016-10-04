from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
# Create your models here.

class Classroom(models.Model):
    title = models.TextField(max_length= 100, unique=True)
    year = models.IntegerField(default = datetime.now().year)
    semester = models.TextField(max_length=20)
    slug= models.TextField(max_length=20)
    
    def __unicode__(self):
        return '%s'% self.title

    def get_absolute_url(self):
        return reverse('teaching:view_classroom', kwargs= {'slug': self.slug })

class Announcement(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    slug = models.ForeignKey('teaching.Classroom')
    
    def __unicode__(self):
        return "{}-{}".format(self.date,self.body)

class Scheduled(models.Model):
    date = models.DateField()
    title = models.TextField()
    slug = models.ForeignKey('teaching.Classroom')
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)

    def __unicode__(self):
        return "{}-{}".format(self.date,self.title)
    
# class Document(models.Model):
#     classroom = models.ForeignKey('teaching.Scheduled')
#     upload_location = "uploads/" + classroom + "/%Y/"
#     upload = models.FileField(upload_to=upload_location)
#     date = models.ForeignKey('teaching.Scheduled') 
    
