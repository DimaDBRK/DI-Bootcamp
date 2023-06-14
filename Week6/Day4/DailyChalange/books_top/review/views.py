from django.shortcuts import render
from typing import Any, Dict
from django.shortcuts import render, redirect
from datetime import date
from .models import Book, BookReview
from .forms import BookForm, BookReviewForm
from django.views.generic.edit import CreateView, DeleteView, FormMixin
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

from django.shortcuts import get_object_or_404


from django.db.models import Q
from django.db.models import Avg

# Create your views here.
class HomePageView(ListView):
    model = Book
    template_name = 'homepage.html'
    context_object_name = 'books'
    

class AddBookView(CreateView): #we check if user is login, if no - ask login, redirect 
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('homepage')
    login_url = reverse_lazy('login') #redirect to ligin page
    redirect_field_name = reverse_lazy('homepage')
    
    
    
class BookReviewCreateView(CreateView):
    model = BookReview
    form_class = BookReviewForm
    template_name = 'add_review.html'
    success_url = reverse_lazy('homepage')

    
    def get_context_data(self, **kwargs):
        book = Book.objects.get(id = self.kwargs['pk'])
        reviews = book.reviews.all()

        context = super().get_context_data(**kwargs)
        context['book'] = book
        
        return context

    def form_valid(self, form):
        return super().form_valid(form) 
    
    
    def get_initial(self, **kwargs): # sets the ininital values for the form of the view
        user = self.request.user #get current user
        book = Book.objects.get(id = self.kwargs['pk'])
        # user1 = UserProfile.objects.get(user = self.request.user)
        # print(user1)
        return {'user' : user,
                'book': book}
    
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_id.html' 
    success_url = reverse_lazy('homepage')
    context_object_name = 'book' 

    def get_context_data(self, **kwargs):
        book = Book.objects.get(id = self.kwargs['pk'])
        reviews = book.reviews.all()

        context = super().get_context_data(**kwargs)
        context['reviews'] = reviews
        context['avg_rating'] = reviews.aggregate(Avg('raiting'))['raiting__avg']
        return context
    
    