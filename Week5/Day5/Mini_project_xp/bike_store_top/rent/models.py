from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.first_name

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey('VehicleType', on_delete= models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.FloatField(blank=True, null=True)
    size  = models.ForeignKey('VehicleSize', on_delete= models.CASCADE)
    
    def __str__(self):
        return f'{self.id} type {self.vehicle_type}'
    
class VehicleType(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class VehicleSize(models.Model):
    name = models.CharField(max_length=50, null=True) 

    def __str__(self):
        return f'size {self.name}'

class Rental(models.Model):
    rental_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    customer =  models.ForeignKey('Customer', on_delete= models.CASCADE) #(foreign key to Customer)
    vehicle = models.ForeignKey('Vehicle', on_delete= models.CASCADE) #(foreign key to Vehicle)
   
    
    def __str__(self):
        return f'{self.id} return on {self.return_date}'

class RentalRate(models.Model):
    daily_rate = models.FloatField(blank=True, null=True)
    vehicle_type =  models.ForeignKey('VehicleType', on_delete= models.CASCADE) #(foreign key to foreign key to Vehicle Type)
    vehicle_size  = models.ForeignKey('VehicleSize', on_delete= models.CASCADE) #(foreign key to foreign key to Vehicle Size))
    
    def __str__(self):
        return f'rent {self.daily_rate}'
    
    
class RentalStation(models.Model):    
    name = models.CharField(max_length=50, null=True) 
    capacity = models.IntegerField(null=True) #(amount of vehicles it can store)
    address =  models.ForeignKey('Address', on_delete= models.CASCADE)  #(foreign key to Address)
    
    def __str__(self):
        return self.name
    
    
    
class Address(models.Model):  
    address = models.CharField(max_length=50, null=True) 
    address2 = models.CharField(max_length=50, blank = True, null=True) 
    city = models.CharField(max_length=50, blank = True, null=True) 
    country = models.CharField(max_length=50, blank = True, null=True) 
    postal_code = models.IntegerField(blank = True,null=True) 
    
    def __str__(self):
        return self.address
    
    
    
      
    