from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    description = models.TextField(max_length=150)
    page_count = models.IntegerField()
    categories = models.CharField(max_length=50)
    thumbnail_url = models.URLField(blank=True, null=True)
 
    
class BookReview(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name= 'reviews' )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'users')
    raiting = models.IntegerField(default=0, blank = True, null= True,  validators=[
                                                                        MaxValueValidator(5),
                                                                        MinValueValidator(0)
                                                                                  ])
    review = models.TextField(max_length=150, blank = True, null= True)
    
