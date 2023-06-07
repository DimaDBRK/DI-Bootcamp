import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
import random
django.setup()

from rent.models import Customer, RentalRate, VehicleType, VehicleSize, Vehicle, Rental
from faker import Faker

fake = Faker(locale=['en_US', 'it_IT', 'fr_FR'])

def create_customers(number:int):

    for _ in range(number):

        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.msisdn()
        address = fake.address()

        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            email = email,
                            phone_number = phone_number, 
                            address = address)
        customer.save()

    print(f"CREATED {number} Customers")
    
def create_city():
    items = Customer.objects.all()
    for customer in items:
       
        city = fake.city()
        country = fake.country() 
       
        customer.city = city
        customer.country = country
    
        customer.save()

        print(city, country )


def create_rent_rate():
    
    # class RentalRate(models.Model):
    # daily_rate = models.FloatField(blank=True, null=True)
    # vehicle_type =  models.ForeignKey('VehicleType', on_delete= models.CASCADE) #(foreign key to foreign key to Vehicle Type)
    # vehicle_size  = models.ForeignKey('VehicleSize', on_delete= models.CASCADE) #(foreign key to foreign key to Vehicle Size))
    
    types = {"bike":10.4, "electric bike":11.3, "scooter":15.6, "jetpack":18.7}
    sizes = {"small":1, "medium":2, "large":3, "double":4}
    
    renat = RentalRate.objects.all()
    type_objects = VehicleType.objects.all()
    size_objects = VehicleSize.objects.all()
    
    for item_t in type_objects:
        for itmem_s in size_objects:
            item_t.name
            itmem_s.name
            # print(types[item_t.name])
            rent_rate = round(types[item_t.name] * sizes[itmem_s.name],2)
            print(item_t, itmem_s,rent_rate )
    
            renat = RentalRate(daily_rate = rent_rate, vehicle_type = item_t, vehicle_size = itmem_s)
            renat.save()

# rentals using 
# return date should sometimes be null
# return date (if not null) must be after rental date
# neither of these dates may be in the future
# if a vehicle is already rented and has not been returned, it should not be used for a new rental.

def create_rentals_using(num:int):
    
    for _ in range(num):
        rental_date = fake.date_this_year()
        while True: 
            return_date = fake.date_this_year()
            if return_date > rental_date:
                break
        all_customers = Customer.objects.all()
             
        customer = random.choice(all_customers)
            
        
        all_vehiclies = Vehicle.objects.all()
        vehicle = random.choice(all_vehiclies)
           
        
        rent_item = Rental(rental_date = rental_date,
                            return_date = return_date,
                            customer = customer,
                            vehicle = vehicle
                            )
        rent_item.save()
                
        print(rental_date, return_date, customer, vehicle)
        
         
# add some nulls
    all_rents = Rental.objects.all()
    for _ in range(50):
        rent_item = random.choice(all_rents)
        rent_item.return_date = None
        rent_item.save()

def create_Vehicle(num:int):
    
    for _ in range(num):
        all_vehiclies_type = VehicleType.objects.all()
        all_vehiclies_size = VehicleSize.objects.all()
        
        vehicle_type = random.choice(all_vehiclies_type)
        size = random.choice(all_vehiclies_size)
        real_cost = random.randint(5000, 10000)
        
        vec_item = Vehicle(vehicle_type = vehicle_type,
                                size = size,
                                real_cost = real_cost,
                            )
        vec_item.save()
    


  
# create_customers(100)
# create_city()
# create_rent_rate()

# create_rentals_using(100)
# create_Vehicle(99)
