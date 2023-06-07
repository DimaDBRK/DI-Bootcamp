from django.shortcuts import render, redirect
from datetime import date
from .models import Film, Director
from .forms import FilmForm, DirectorForm #FavouriteFilmForm
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, View, DetailView
from django.urls import reverse_lazy 
from django.views.generic.list import ListView
from django.db.models import Q #to lool up for multiple filter (complex filters)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin,
                                        PermissionRequiredMixin)


from django.contrib import messages
import requests
from django.contrib.messages.views import SuccessMessageMixin
from accounts.models import UserProfile
from django.shortcuts import get_object_or_404

# Create your views here.
class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'


class FilmCreateView(CreateView):
    model = Film
    # fields = '__all__'
    form_class = FilmForm
    template_name = 'film_form.html'
    success_url = reverse_lazy('homepage')


class DirectorCreateView(CreateView):
    model = Director
    # fields = '__all__'
    form_class = DirectorForm
    template_name = 'director_form.html'
    success_url = reverse_lazy('homepage')
    
    # def get_initial(self): # sets the ininital values for the form of the view
    #     return {'title':'post !!!',
    #             'content':'weather',
    #             'autor' : current_user


class FilmDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    
    def test_func(self): #<-----function that returns True/False when user tries to reach the view
        
        if self.request.user.is_superuser   :
            
            return True
           
        else:
            return False #<-----Leads to a 403 (forbidden) page
        
    success_message = "Delete was created successfully"
    model = Film
    template_name = 'delete_film.html'
    success_url = reverse_lazy('confirm_delete')
    
def conf_delete(request):
    return render(request, 'confirm_delete.html')


class FavoriteFilmView(View):
   
    def post(self,request, film_id): 
        
        film = get_object_or_404(Film, id=film_id)
        user = self.request.user
        user_profile = user.user_profile
        print(user_profile)

        if film in user_profile.favorite_films.all():
            user_profile.favorite_films.remove(film)
            messages.success(request, "Film removed from favorites.")
        else:
            user_profile.favorite_films.add(film)
            messages.success(request, "Film added to favorites.")
            
        return redirect('homepage')


class FilmDetailView(DetailView):
    model = Film
    template_name = 'filmdetail.html'
    context_object_name = 'film'
        

# class AddFavouriteFilmView(CreateView):
#     model = UserProfile
#     form_class = FavouriteFilmForm
#     template_name = 'film_favourite.html'
#     success_url = reverse_lazy('homepage')


#     def get_initial(self): # sets the ininital values for the form of the view
#         user = self.request.user #get current user
#         film = Film.objects.get(id = self.kwargs["pk"])
#         return {'user' : user,
#                 'favorite_films' : film}
       

# class DeleteFavouriteFilmView(DeleteView):
#     model = UserProfile
#     form_class = FavouriteFilmForm
#     template_name = 'film_favourite.html'
#     success_url = reverse_lazy('homepage')


#     def get_initial(self): # sets the ininital values for the form of the view
#         user = self.request.user #get current user
#         film = Film.objects.get(id = self.kwargs["pk"])
#         return {'user' : user,
#                 'favorite_films' : film} 