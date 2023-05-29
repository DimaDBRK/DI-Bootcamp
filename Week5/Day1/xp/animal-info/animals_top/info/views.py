from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import json
import os

# Create your views here.
def family_get(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # JSON file
    f = open (dir_path+"\\" +'animal_info.json', "r")
  # Reading from file
    data = json.load(f)
  # Iterating through the json
    id = 3
    list_animals = []
    for item in data['animals']:
        if item['family'] == id :
            list_animals.append(item['name'])
    
    for item in data['families']:
        if item['id'] == id :
            id_name = item['name']
       
# coolect data
    f.close()
    
    today =  date.today()

    content = {
        'id': id,
        'time': today,
        'id_name': id_name,
        'list_animals': list_animals,
    }
    
    f.close()
    
    return render(request, 'family/3.html', content)


def animal_get(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # JSON file
    f = open (dir_path+"\\" +'animal_info.json', "r")
  # Reading from file
    data = json.load(f)
  # Iterating through the json
    an_id = 1
   
    for item in data['animals']:
        if item['id'] == an_id :
            res = item
            print(item)
    
    for item in data['families']:
        if item['id'] == res['family'] :
            id_name = item['name']
       
# coolect data
    f.close()
    
    today =  date.today()
        

    content1 = {
        'an_id': an_id,
        'time': today,
        'id_name': id_name,
        'res': res,
    }
    
    f.close()
    
    return render(request, 'animal/1.html', content1)