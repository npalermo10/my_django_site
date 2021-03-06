
from __future__ import unicode_literals
from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from datetime import timedelta, date

class Post(models.Model):

    # def get_image_path(instance, filename):
        # return os.path.join('pictures', str(instance.id), filename)

    image = models.ImageField(upload_to="pictures/blog_pics", blank=True, null=True)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')
  
    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('blog:view_blog_post', kwargs= {'slug': self.slug })

    def recent_post(self):
        if self.posted + timedelta(days=30) >= date.today():
            return True
        else:
            return False

    
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title
    
    def get_absolute_url(self):
        return reverse('blog:view_blog_category', kwargs= {'slug': self.slug})

