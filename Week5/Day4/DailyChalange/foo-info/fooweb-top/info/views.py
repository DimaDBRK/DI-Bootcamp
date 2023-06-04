from django.shortcuts import render
from info.models import Person
from .forms import PersonForm
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

def search_by(request) :
     if request.method == 'POST':
        form = request.POST
        filled_form = PersonForm(form)
        filled_form.save()
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            name = form.cleaned_data['name']

            if phone_number :
                people = Person.objects.filter(phone_number=phone_number)
            elif name :
                people = Person.objects.filter(name__icontains=name)
            else:
                people = Person.objects.none()

            return render(request, 'person_search_results.html', {'people': people, 'form': form})
    
        else:
            form = PersonForm()
            context = {'form': form}
        return render(request, 'person_search.html', context)