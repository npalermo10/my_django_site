from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Publication(models.Model):
    citation = models.TextField(max_length = 2000, unique=True)
    year = models.IntegerField(default = datetime.now().year)
    
    def __unicode__(self):
        return '%s'% self.citation

class Award(models.Model):
    description = models.TextField(max_length = 2000, unique=True)
    date = models.DateField()
    
    def __unicode__(self):
        return '%s'% self.description
    
