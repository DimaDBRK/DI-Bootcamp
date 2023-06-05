from django.shortcuts import render
from datetime import date
from .models import Film, Director, Review
from .forms import FilmForm, DirectorForm, ReviewForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 
from django.views.generic.list import ListView
from django.db.models import Q #to lool up for multiple filter (complex filters)
from typing import Any, Dict

# Create your views here.
class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #for mofdify the context dictonary - we add new feature
    #     context =  super().get_context_data(**kwargs) #getting the current context
       
    #     review = Review.objects.all()
    #     context['review'] = review
    #     print(review)
    #     return context



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
    #             'autor' : current_use

class ReviewCreateView(CreateView):
    model = Review
    # fields = '__all__'
    form_class = ReviewForm
    tempalte_name = 'review_form.html'
    success_url = reverse_lazy('homepage')
    
    def get_initial(self): # sets the ininital values for the form of the view
        return {'rating': 5,}
                