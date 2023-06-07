from django.db import models
from datetime import datetime, date
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.
class RegisterView(CreateView): #SignupForm:
    form_class = RegisterForm
    model = User
    tempalte_name = 'user_form.html'
    success_url = reverse_lazy('login')


    #user Profile customization
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one field
#     birth_date = models.DateField()
   

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'

#     def person_age(self):
#         current_date = date.today()
#         current_age = current_date.year-self.birth_date.year
#         return f'{current_age}'


@login_required
def profile(request, id):
  user = User.objects.get(id=id)
  return render(request, 'profile.html', {'user': user})


