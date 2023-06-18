from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

import datetime

# from accounts.models import UserProfile
# Create your models here.

# How to connect to user???
# class Guest(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     email = models.EmailField(unique=True, blank=True, null=True)
#     phone_number = models.CharField(max_length=50, blank=True, null=True)
#     # address = models.CharField(max_length=100,blank=True, null=True)
#     city = models.CharField(max_length=50, blank=True, null=True)
#     # country = models.CharField(max_length=50, blank=True, null=True)
    
#     def __str__(self):
#         return self.first_name
    
# class Room(models.Model):
#     room_number = models.IntegerField(validators=[
#                                     MaxValueValidator(100),
#                                     MinValueValidator(600)
#                                     ]
#     )
#     room_type = models.ForeignKey('RoomType', on_delete= models.CASCADE)
#     date_created = models.DateField(auto_now_add=True)
#     room_cost = models.FloatField(blank=True, null=True)
#     room_size  = models.ForeignKey('RoomSize', on_delete= models.CASCADE)
    
#     def __str__(self):
#         return f'№ {self.room_number}'
    
# class RoomType(models.Model):
#     name = models.CharField(max_length=50, null=True)

#     def __str__(self):
#         return self.name


# class RoomSize(models.Model):
#     name = models.CharField(max_length=50, null=True) 

#     def __str__(self):
#         return f'size {self.name}'
    

# class Reservation(models.Model):
#     check_in  = models.DateField(blank=True, null=True)
#     check_out = models.DateField(blank=True, null=True)
#     guest =  models.ForeignKey('Guest', on_delete= models.CASCADE, related_name= 'guest_reservations') #(foreign key to )
#     room = models.ForeignKey('Room', on_delete= models.CASCADE, related_name= 'room_reservations') #(foreign key to )
   
    
#     def __str__(self):
#         return f'{self.id} return on {self.return_date}'


# class Review(models.Model):
#     author = models.ForeignKey('Guest', on_delete= models.CASCADE, related_name= 'reviews')
#     review_text = models.TextField(max_length=200)
#     star = models.IntegerField(default=1, 
#                                     validators=[
#                                     MaxValueValidator(5),
#                                     MinValueValidator(1)
#                                     ]
#                                 ) #an integer field to provide a rating (1-5)
#     review_date = models.DateTimeField(auto_now_add=True)
   

class Room(models.Model):

    class RoomType(models.IntegerChoices):
        SINGLE = 1
        DOUBLE = 2
        TRIPLE = 3
        QUAD = 4

    room_type = models.PositiveSmallIntegerField(
        choices=RoomType.choices,
        default=RoomType.SINGLE
    )
    price = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"Room #{self.room_number}"


class Booking(models.Model):
    guest = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    guests_num = models.IntegerField(
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
    )
    room = models.ForeignKey(Room, related_name='booking', on_delete=models.CASCADE, blank=True)

    def check_availability(self):
        rooms = Room.objects.filter(room_type=self.guests_num)

        for room in rooms:
            self.room = room

            for booking in self.room.booking.all():
                if self.check_in > booking.check_in > self.check_out:
                    return True
                elif booking.check_out > self.check_in and booking.check_in < self.check_out:
                    return True
                elif booking.check_in < self.check_in and booking.check_out > self.check_out:
                    return True
        return False

    def clean(self):
        if self.check_in < datetime.date.today():
            raise ValidationError("The check in date cannot be in the past!")
        elif self.check_in >= self.check_out:
            raise ValidationError("The check out date have to come after the check in date!")
        elif self.check_availability():
            raise ValidationError("The date range you picked is not available!")

    def save(self, *args, **kwargs):
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.guest}: {self.check_in} - {self.check_out}"


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()