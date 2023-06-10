from django.db.models.signals import post_save #signal to save new user profile to database
from django.dispatch import receiver #signal to save new user profile to database
from django.contrib.auth.models import User, Group
from .models import UserProfile, Image

#User => post save signal -> reciver function -> New UserProfile

# def create_user_profile(sender, instance, created, **kwargs):



# In apps add -  def ready(self):
#         import accounts.signals

@receiver(post_save, sender = User) # we need to change in apps
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        

@receiver(post_save, sender = Image) # we need to change in apps
def increase_image_qty(sender, instance, created, **kwargs):
    if created:
        user_image = instance.author
        item = UserProfile.objects.get(user = user_image)
        item.images_number += 1
        item.save()
        
      