from django.db import models
from datetime import datetime 

# Create your models here.
class Gif(models.Model):
# model - table
    title = models.CharField(max_length=100) 
    url   = models.URLField()
    uploader_name   = models.CharField(max_length=50, null=True) 
    created_at   = models.DateTimeField(default=datetime.now, blank=True) #should be populated when created
    # category = models.ManyToManyField('Category')
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField('Gif', related_name='categories', blank=True)
    
    def __str__(self):
        return {self.name}
