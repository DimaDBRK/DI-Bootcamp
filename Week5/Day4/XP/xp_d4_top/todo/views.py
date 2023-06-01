from django.shortcuts import render
from datetime import date
from .models import Todo, Category
from .forms import TodoForm, DoneForm, CategoryForm

# Create your views here.
def add_todo_view(request):
    
    if request.method == 'POST':
        data = request.POST
        filled_form = TodoForm(data)
        if filled_form.is_valid():
            filled_form.save()
        else:
            print(filled_form.errors)
         
    #Get
    post_form = TodoForm(initial={'title':'New todo'})
    
    context = {'form':post_form}
    
    return render(request, 'add_todo.html', context)

def add_category_view(request):
    
    if request.method == 'POST':
        data = request.POST
        filled_form = CategoryForm(data)
        if filled_form.is_valid():
            filled_form.save()
        else:
            print(filled_form.errors)
         
    #Get
    post_form = CategoryForm()
    
    context = {'form':post_form}
    
    return render(request, 'add_category.html', context)

def display_todos (request):
    # this view will display all the todos from the database.
    today =  date.today()
    todos_info = Todo.objects.all().order_by('title')
    category_info = Category.objects.all()  
    
    if request.method == 'POST':
        data = request.POST
        # filled_form = DoneForm(data)
        
        if (data['Done']).isnumeric():
            id = int(data['Done'])
            todo = todos_info.get(id=id)
            if todo.has_been_done:
                todo.has_been_done = False
                todo.date_completion = None
            else:
                todo.has_been_done = True
                todo.date_completion = today
            todo.save()
            print(todo.id, todo.has_been_done)
        # print(filled_form)
        # print('POST:', data)
    # print()
    # name = request.GET['name']
    
    # post_form = None
    
    context ={'todos': todos_info,
              'category': category_info,
              'today': today,
              }
    
    return render(request, 'dispaly_todos.html', context)


def display_todos_v2 (request):
    # this view will display all the todos from the database.
    today =  date.today()
  
   
    
    if request.method == 'POST':
        data = request.POST
        print(data)
        todo = Todo.objects.get(id = data['isinstance'])
        print(todo)
        todo.has_been_done = True
        todo.date_completion = date.today()
        todo.save()
        
    
    todo_list = Todo.objects.all().order_by('title')  
    todo_forms = []
    for todo in todo_list:
        form = DoneForm(initial = {'isinstance': todo})
        todo_forms.append((todo, form))
   
    
    context ={'todos_forms': todo_forms,
              'today': today,
              }
    
    return render(request, 'dispaly_todos_v2.html', context)




def done_todo_view(request,  id : int):
    today =  date.today()
    todos_info = Todo.objects.all().order_by('title')
    category_info = Category.objects.all()  
    
    todo = todos_info.get(id = id) #get by id
    category_id = Category.objects.get(name = todo.category) ## Get the category by it's id
 
    if todo.has_been_done:
        todo.has_been_done = False
        todo.date_completion = None
    else:
        todo.has_been_done = True
        todo.date_completion = today
    todo.save()
    print(todo.id, todo.has_been_done)
         
   
    
    context ={'todos': todos_info,
              'category': category_info,
              'today': today,
              }
    
    return render(request, 'dispaly_todos.html', context)