from django.db import models

#Project animal info

class Animal(models.Model):
# model - table
    name = models.CharField(max_length=20, default='animal') #no in task, but we shoud add
    legs  = models.ImageField(null=True) #an integer, the number of legs the animal has
    weight  = models.FloatField(null=True) #the average weight of an adult animal of this type
    height  = models.FloatField(null=True) #the average height of an adult animal of this type
    speed  = models.FloatField(null=True) #the maximum speed at which this animal can move
    family  = models.ForeignKey('Family', on_delete= models.SET_NULL, null=True) #he family to which this animal belongs. (Must reference the Family model - see below).

class Family(models.Model):
# model - table
    name = models.CharField(max_length=30)
