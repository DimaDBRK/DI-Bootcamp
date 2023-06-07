from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.views.generic.edit import CreateView, DeleteView


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey('Country', on_delete= models.CASCADE) #One to Many relationship with Country (the “nationality of the film”)
    available_in_countries = models.ManyToManyField('Country', related_name='nationality_film') #Many to Many relationship with Country
    category = models.ManyToManyField('Category')
    director = models.ManyToManyField('Director')
    producers = models.ManyToManyField('Producer')
    
    def __str__(self):
        return self.title

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.last_name
    

#Daily Chalange

class Review(models.Model):
    film = models.ForeignKey('Country', on_delete= models.CASCADE) 
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(default=1, 
                                    validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(1)
                                    ]
                                ) #an integer field to provide a rating (1-5)
    review_date = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return f'review {self.id} {self.film}'
    


class Producer(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
    