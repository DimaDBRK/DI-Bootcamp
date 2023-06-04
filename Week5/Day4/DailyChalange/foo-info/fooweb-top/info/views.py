from django.shortcuts import render, redirect
from info.models import Person
from .forms import SearchForm
from django.db.models import Q

# Create your views here.
def phone_sh(request, phone_number):
    try:
        people_info = Person.objects.get(phone_number = str(phone_number))
        context = {'info': people_info,
                   'check': True}
    except:
        context = {}
  
    return render(request, 'phone_sh.html', context)

def name_sh(request, name):
    try:
        people_info = Person.objects.get(name = name)
        context = {'info': people_info,
                   'check': True}
    except:
        context = {}
  
    return render(request, 'name_sh.html', context)


def search_phone(request):
    
    if request.method == 'POST':
        form = request.POST
        search = form['query']
        print(search)

        if Person.objects.filter(Q(phone_number = search) | Q(name = search) ).exists():
            #There is person go to page with ID
            print('OK')
                       
        return redirect(f'/persons/{search}')
       
             
    return render(request, 'search.html')