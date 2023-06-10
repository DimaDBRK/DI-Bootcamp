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
from django.shortcuts import get_object_or_404
from typing import Any, Dict

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
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #for mofdify the context dictonary - we add new feature
        context =  super().get_context_data(**kwargs) #getting the current context
       
        user_profile = UserProfile.objects.all()
        context['userprofile'] = user_profile
        
        return context
    
    

class AddImageView(CreateView): #we check if user is login, if no - ask login, redirect 
    model = Image
    form_class = ImageForm
    template_name = 'image_share/upload_image.html'
    success_url = reverse_lazy('homepage')
    login_url = reverse_lazy('login') #redirect to ligin page
    redirect_field_name = reverse_lazy('homepage')
    
    def get_initial(self): # sets the ininital values for the form of the view
        user = self.request.user #get current user
        # user1 = UserProfile.objects.get(user = self.request.user)
        # print(user1)
        return {'author' : user }
    
    
class MyImagesView(UserPassesTestMixin, ListView):
    template_name = 'image_share/my_images.html'
    context_object_name = 'images'
    model = Image

    def get_queryset(self):
        return Image.objects.filter(author=self.request.user).all()

    def get_context_data(self, **kwargs):
        context = super(MyImagesView, self).get_context_data(**kwargs)
        context['title'] = "My Images"
        return context

    def test_func(self):
        return self.request.user.is_authenticated
    

class UserProfileView(DetailView):
    template_name = 'image_share/profile_id.html'
    context_object_name = 'profile'
    model = UserProfile
   
    # def post(self,request, film_id): 
        
    #     film = get_object_or_404(Film, id=film_id)
    #     user = self.request.user
    #     user_profile = user.user_profile
    #     print(user_profile)
    
    # def get_context_data(self, **kwargs):
    #     # user = User.objects.get(id=self.kwargs['pk'])
    # #   user = User.objects.get(id=self.kwargs['pk'])
    #     profile = UserProfile.objects.all()
    # #     print('1')
    #     # context = super(UserProfileView, self).get_context_data(**kwargs)
    # #     # context['title'] = f"{user.username}"
    #     # context['profile'] =user
    #     context = user
    #     return context
    

class UserImagesView(ListView):
    template_name = 'image_share/user_images.html'
    context_object_name = 'images'
    model = Image

    def get_queryset(self, **kwargs):
        user_id = User.objects.get(id=self.kwargs['pk'])
        return Image.objects.filter(author= user_id).all()

    # def get_context_data(self, **kwargs):
    #     user = User.objects.get(id=self.kwargs['pk'])
        
    #     context = super(MyImagesView, self).get_context_data(**kwargs)
    #     context['title'] = "My Images"
    #     return context
