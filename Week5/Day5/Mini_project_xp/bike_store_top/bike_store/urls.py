"""
URL configuration for bike_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent.views import (display_rentals, 
                        display_rental_id,
                        display_customer_id,
                        display_all_customers,
                        display_all_vehicles,
                        display_vehicle_id,
                        add_customer_view,
                        add_vehicle_view,
                        add_rental_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/rental/', display_rentals, name='all_rentals'),
    path('rent/rental/<int:id>', display_rental_id),
    path('rent/customer/<int:id>', display_customer_id),
    path('rent/customer/', display_all_customers),
    path('rent/vehicle/', display_all_vehicles),
    path('rent/vehicle/<int:id>', display_vehicle_id),
    path('rent/customer/add', add_customer_view),
    path('rent/vehicle/add', add_vehicle_view),
    path('rent/rental/add', add_rental_view),
]
