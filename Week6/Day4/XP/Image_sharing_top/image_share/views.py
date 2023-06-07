from django.shortcuts import render
from .forms import RegisterForm, ImageForm
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, View, DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin #check for form base
from django.contrib.auth.mixins import UserPassesTestMixin #check for form -> tets function
from .models import UserProfile

from .models import Image
# Create your views here.

class RegisterView(CreateView): #SignupForm:
    form_class = RegisterForm
    model = User
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    

@login_required
def profile(request, id):
  user = User.objects.get(id=id)
  return render(request, 'registration/profile.html', {'user': user})


class HomePageView(ListView):
    model = Image
    template_name = 'homepage.html'
    context_object_name = 'images'
    

class AddPostView(CreateView): #we check if user is login, if no - ask login, redirect 
    model = Image
    form_class = ImageForm
    template_name = 'image_share/upload_image.html'
    success_url = reverse_lazy('homepage')
    login_url = reverse_lazy('login') #redirect to ligin page
    # redirect_field_name = reverse_lazy('posts')
    
    # def get_initial(self): # sets the ininital values for the form of the view
    #     user = self.request.user #get current user
    #     user_profile = user.userprofile #the current user profile
    #     return {'author' : user_profile}