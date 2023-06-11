from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=60)
    publish_date = models.DateField()
    description = 
    page_count = 
    categories = 
    thumbnail_url  =
    
    
    
    content = models.TextField()
    
    author = models.ForeignKey(UserProfile, on_delete= models.CASCADE, related_name= 'posts')
    
    data_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category') # many to many
