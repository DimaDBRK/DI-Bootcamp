from django.db import models
#from phonenumber_field.formfields import PhoneNumberField # problem with installation


# Create your models here.

class Person(models.Model):
# id - auto
    name = models.CharField(max_length=50) #(String)
    email  = models.CharField(unique=True) #(String, unique)
    phone_number  = models.CharField(blank=True) #Problem with django-phonenumber-field package.
    address   = models.CharField(null=True) 
  
