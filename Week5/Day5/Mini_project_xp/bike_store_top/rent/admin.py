from django.contrib import admin
from .models import Address, Customer, Vehicle, VehicleType, VehicleSize, Rental, RentalRate, RentalStation
                     

# Register your models here.

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(VehicleType),
admin.site.register(VehicleSize),
admin.site.register(Rental),
admin.site.register(RentalRate),
admin.site.register(RentalStation)




