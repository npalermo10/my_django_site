from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Curr_research(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    start_date = models.DateField(db_index=True)
    category = models.ForeignKey('current_research.Category')

    def __unicode__(self):
        return '%s'% self.title
    
class Category(models.Model):
    title = models.CharField(max_length = 100,db_index = True)
    slug = models.SlugField(max_length = 100, db_index = True)
    
    def __unicode__(self):
        return '%s'% self.title
    
