from django.shortcuts import render
from datetime import date
from .models import Film, Director
from .forms import FilmForm, DirectorForm 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 
from django.views.generic.list import ListView
from django.db.models import Q #to lool up for multiple filter (complex filters)

# Create your views here.
class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'


class FilmCreateView(CreateView):
    model = Film
    # fields = '__all__'
    form_class = FilmForm
    tempalte_name = 'film_form.html'
    success_url = reverse_lazy('homepage')


class DirectorCreateView(CreateView):
    model = Director
    # fields = '__all__'
    form_class = DirectorForm
    tempalte_name = 'director_form.html'
    success_url = reverse_lazy('homepage')
    
    # def get_initial(self): # sets the ininital values for the form of the view
    #     return {'title':'post !!!',
    #             'content':'weather',
    #             'autor' : current_user