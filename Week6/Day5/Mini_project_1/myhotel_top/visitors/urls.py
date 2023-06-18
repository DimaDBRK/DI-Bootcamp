from django.contrib import admin
from django.urls import path
from .views import (HomePageView, InfoPageView, RoomsView, OrderView, contact
                       
                        )       

urlpatterns = [
    # path('aboutus/', AboutUs.as_view(), name = 'aboutus'),
    path('', HomePageView.as_view(), name='home'),
    path('info/', InfoPageView.as_view(), name='info'),
    path('booking/', RoomsView.as_view(), name='booking'),
    path('order/<int:pk>', OrderView.as_view(), name='order'),
    path('contact/', contact, name='contact'),
   
]