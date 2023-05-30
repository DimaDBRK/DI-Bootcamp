from django.shortcuts import render
from info.models import Person

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

