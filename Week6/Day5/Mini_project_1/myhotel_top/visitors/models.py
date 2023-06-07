from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import UserProfile
# Create your models here.

# How to connect to user???
class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    # address = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    # country = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.first_name
    
class Room(models.Model):
    room_number = models.IntegerField(validators=[
                                    MaxValueValidator(100),
                                    MinValueValidator(600)
                                    ]
    )
    room_type = models.ForeignKey('VehicleType', on_delete= models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    room_cost = models.FloatField(blank=True, null=True)
    room_size  = models.ForeignKey('VehicleSize', on_delete= models.CASCADE)
    
    def __str__(self):
        return f'№ {self.room_number}'
    
class RoomType(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class RoomSize(models.Model):
    name = models.CharField(max_length=50, null=True) 

    def __str__(self):
        return f'size {self.name}'
    

class Reservation(models.Model):
    check_in  = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    guest =  models.ForeignKey('Guest', on_delete= models.CASCADE, related_name= 'guest_reservations') #(foreign key to )
    room = models.ForeignKey('Room', on_delete= models.CASCADE, related_name= 'room_reservations') #(foreign key to )
   
    
    def __str__(self):
        return f'{self.id} return on {self.return_date}'


class Review(models.Model):
    author = models.ForeignKey('Guest', on_delete= models.CASCADE, related_name= 'reviews')
    review_text = models.TextField(max_length=200)
    star = models.IntegerField(default=1, 
                                    validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(1)
                                    ]
                                ) #an integer field to provide a rating (1-5)
    review_date = models.DateTimeField(auto_now_add=True)
   
    
    