from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image (models.Model):
# model - table
    image = models.ImageField(upload_to ='images/')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'images')
    data_create = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name= 'userprofile')
    images_number = models.IntegerField(default=0, blank = True, null= True)
    
    def __str__(self):
        return f'Profile: {self.user.username}'