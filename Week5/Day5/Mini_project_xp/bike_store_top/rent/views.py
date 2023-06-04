from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
from .models import Customer, Vehicle, VehicleType, VehicleSize, Rental, RentalRate
from .forms import CustomerForm, VehicleForm, RentalForm, ReturnForm
# from .forms import CategoryForm, PostForm, SearchForm
# Create your views here.

def display_rentals(request):
    # 1./rent/rental/ - show a list of all rentals, unreturned 
    # first, then ordered by date ascending (earliest first)
    today =  date.today()
    rentals_info = Rental.objects.all().order_by('rental_date')
   
       
    context ={'rentals': rentals_info,
           
              'today': today,
              }
    
    return render(request, 'display_rentals.html', context)

def display_rental_id(request, id: int):
    #  show the information about the given rental:
    # customer details
    # vehicle details
    # rental details (“Returned on: <date>” / “Not yet returned”)
    today =  date.today()
    rental = Rental.objects.get(id =id)
    customer = rental.customer
    vehicle = rental.vehicle
    
    if request.method == 'POST':
        data = request.POST
        rental_for_update  = Rental.objects.get(id = data['isreturn'])
        
        print(data['isreturn'])
        rental_for_update.return_date = today
       
        rental_for_update.save()
    
    post_form = ReturnForm(initial = {'isreturn': rental})  
    
       
    context ={'rental': rental,
              'customer': customer,
              'vehicle': vehicle,
              'rental_form': post_form
            }
    
    return render(request, 'display_rental_id.html', context)


def display_customer_id(request, id: int):
    # 
    
    customer = Customer.objects.get(id =id)
    
       
    context ={'customer': customer
                }
    
    return render(request, 'display_customer_id.html', context)


def display_all_customers(request):
    # show the customer matching the given ID
    
    customers_all = Customer.objects.all().order_by('first_name')
    today =  date.today()
       
    context ={'customers': customers_all,
               'today': today,
                }
    
    return render(request, 'display_all_castomers.html', context)

def display_all_vehicles(request):
    # 
    
    vehicles_all = Vehicle.objects.all()
    types_all = VehicleType.objects.all().order_by('name')
    rental_all = Rental.objects.all()
    list = []
    for item in vehicles_all:
        notavalible_status = Rental.objects.filter(vehicle = item,return_date = None).exists()
        list.append((item, notavalible_status))
    today =  date.today()
       
    context ={'vehicles': vehicles_all,
              'types': types_all,
               'vehicles_status': list,
               'today': today,
                }
    
    return render(request, 'display_all_vehicles.html', context)

def display_vehicle_id(request, id: int):
    # also show whether it’s currently being rented
    
    vehicle_id = Vehicle.objects.get(id =id)
    rental_check =  Rental.objects.filter(vehicle=vehicle_id).exists()
    if rental_check:
        rental_info = Rental.objects.filter(vehicle=vehicle_id)[0]
    else:
        rental_info = None
    
    print(id, rental_info)        
    context ={'vehicle': vehicle_id,
              'rental': rental_info,
            
                }
    
    return render(request, 'display_vehicle_id.html', context)


def add_customer_view(request):
   
    if request.method == 'POST':
        data = request.POST
        filled_form = CustomerForm(data)
        if filled_form.is_valid():
            filled_form.save()
        else:
            print(filled_form.errors)
         
    #Get
    post_form = CustomerForm(initial={'first_name':'New customer'})
    
    context = {'form':post_form}
    
    return render(request, 'add_customer.html', context)
 
 
def add_vehicle_view(request):
   
    if request.method == 'POST':
        data = request.POST
        filled_form = VehicleForm(data)
        if filled_form.is_valid():
            filled_form.save()
        else:
            print(filled_form.errors)
         
    #Get
    post_form = VehicleForm(initial={'first_name':'New customer'})
    
    context = {'form':post_form}
    
    return render(request, 'add_vehicle.html', context)

 
def add_rental_view(request):
# rent/rental/add – provide a form to enter a customer ID and
# a vehicle ID to create a rental.
# If the customer or the vehicle does not exist, 
# show a user-friendly error message.
# If the vehicle is currently being rented, 
# show a relevant error message.
    error =  None
    
    if request.method == 'POST':
        data = request.POST
        filled_form = RentalForm(data)
        
        
            
        if filled_form.is_valid():
            checked_customer_id = data['customer']
            checked_vehicle_id = data['vehicle']
            try:
                checked_customer = Customer.objects.get(id = checked_customer_id)
                checked_vehicle =  Vehicle.objects.get(id = checked_vehicle_id)
                
                if Rental.objects.filter(vehicle = checked_vehicle,return_date = None).exists():
                    print('It is not free')
                    messages.error(request, 'Vehicle is not avalible.')

                else:
                    messages.success(request, 'Vehicle is OK.')
                    print('It is free')
                    filled_form.save()
                    # return redirect('all_rentals')
                    
                
            # else:
            #     print("Rent")
            #     error = "Vehicle is already rent."
            except Customer.DoesNotExist:
                messages.error(request, 'Invalid customer ID.')
        
            except Vehicle.DoesNotExist:
                messages.error(request, 'Invalid vehicle ID.')      
        
        
        else:
            print(filled_form.errors)
            error = filled_form.errors
    
    today =  date.today()   
    #Get
    post_form = RentalForm(initial={'rental_date': today})
    
    context = {'form':post_form}
    
    return render(request, 'add_rental.html', context)