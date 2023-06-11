from django.db import models

# Create your models here.

#  Student with the following fields:
# first_name
# last_name
# email
# date_joined - the time when the instance is created

class Student(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    date_joined  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'