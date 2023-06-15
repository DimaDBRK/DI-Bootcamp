from django.contrib import admin
from django.urls import path
from .views import ( HomePageView, AddBookView, BookReviewCreateView, BookDetailView)       

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name = 'homepage'),
    path('add-book/', AddBookView.as_view(), name = 'add-book'),
    path('add-review/<pk>', BookReviewCreateView.as_view(), name='add-review'),
    path('details/<pk>', BookDetailView.as_view(), name="book"),
    
  
]