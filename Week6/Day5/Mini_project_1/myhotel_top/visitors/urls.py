from django.contrib import admin
from django.urls import path
from .views import (AboutUs,
                        #  FilmCreateView,
                        #  DirectorCreateView
                        )       

urlpatterns = [
    path('aboutus/', AboutUs.as_view(), name = 'aboutus'),
   
]