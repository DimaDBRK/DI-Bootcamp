from django.shortcuts import render

# Create your views here.

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]


# takes a request, returns a response
def people_get(request):
    
# sort list by age
    newlist = sorted(people, key = lambda d: d['age'], reverse=False)
    context = {'name':'people',
               'people_list': newlist
               }
    
    return render(request, 'people.html', context)

def id_get(request, id):
    
    for items in people:
        if items['id'] == int(id):
            context = items
    
    return render(request, 'people_id.html', context)