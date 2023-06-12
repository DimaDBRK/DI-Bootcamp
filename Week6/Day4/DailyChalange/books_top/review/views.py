from django.shortcuts import render
from typing import Any, Dict
from django.shortcuts import render, redirect
from datetime import date
from .models import Book, BookReview
from .forms import BookForm
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

from django.shortcuts import get_object_or_404

# Create your views here.
class HomePageView(ListView):
    model = Book
    template_name = 'homepage.html'
    context_object_name = 'books'