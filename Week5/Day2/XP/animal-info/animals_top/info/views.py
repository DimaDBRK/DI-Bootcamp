from django.shortcuts import render
from .models import Animal, Family

# Create your views here.
def family_id(request, id):
    #ID (primary key) of the given family. Should show a list of all animals in that family.

    animal_family_id = Animal.objects.filter(family_id = id).values()
  
    family_info = Family.objects.get(id = id)
    context ={'animal_list': animal_family_id,
              'family_name': family_info}
    
    return render(request, 'family.html', context)


def animal_id(request, id):
    #ID (primary key) of the given family. Should show a list of all animals in that family.

    animal_info = Animal.objects.get(id = id)
    family_info = Family.objects.get(id = animal_info.family_id)
        
    
    context ={'animal': animal_info,
              'family': family_info}
    
    return render(request, 'animal.html', context)

def animals_list(request):
    #list of all animals

    animal_list = Animal.objects.all().values()
    family_list = Family.objects.all()
  
    context ={'animal_list': animal_list,
              'family_name': family_list}
    
    return render(request, 'animals.html', context)


def id_get(request, id): #for animal with ID
                   
    animal_info = Animal.objects.get(id = id) #get info for animal with ID
    family_info = Family.objects.get(id = animal_info.family_id) #get info for family name
    context ={'animal': animal_info,
              'family': family_info}
         
    return render(request, 'animal_id.html', context)