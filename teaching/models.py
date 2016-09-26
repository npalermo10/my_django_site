from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Classroom(models.Model):
    title = models.TextField(max_length= 100, unique=True)
    year = models.IntegerField(default = datetime.now().year)

    def __unicode__(self):
        return '%s'% self.title

    def get_absolute_url(self):
        return reverse('teaching:view_classroom', kwargs= {'title': self.title })

class Announcements(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    classroom = models.ForeignKey('teaching.Classroom')
    
    def __unicode__(self):
        return "{}-{}".format(self.date,self.body)

class Scheduled(models.Model):
    date = models.DateField()
    title = models.TextField()
    classroom = models.ForeignKey('teaching.Classroom')

    def __unicode__(self):
        return "{}-{}".format(self.date,self.title)
    
class Document(models.Model):
    upload_location = "uploads/" + self.classroom "/%Y/"
    upload = models.FileField(upload_to=upload_location)
    date = models.ForeignKey('teaching.Scheduled') 
    
