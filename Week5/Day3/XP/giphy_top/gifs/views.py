from django.shortcuts import render
from .models import Gif, Category
from .forms import GifForm, CategoryForm

# Create your views here.
def add_new_gif(request):
   
    if request.method == 'POST':
        form = GifForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            gif_to_add = form.save()
            #return redirect('post_create')
    else:
        form = GifForm()
        
    context = {'form': form}
    
    return render(request, 'newgif.html', context)

def add_new_category(request):
   
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            gif_to_add = form.save()
            #return redirect('post_create')
    else:
        form = CategoryForm()
        
    context = {'form': form}
    
    return render(request, 'newcategory.html', context)

def all_gifs(request):
    # this view will display all the gifs from the database. Display each gif in an img tag.
    gif_info = Gif.objects.all()
    category_info = Category.objects.all()  
    
    context ={'gifs': gif_info,
              'Category': category_info}
    
    return render(request, 'homepage.html', context)


def category_info(request, id : int):
    # Category view: this view accepts a category id as a parameter and displays all gifs with that category (ie. for example all the “happy” gifs).
    current_category = Category.objects.get(id = id) #get category 
    gif_in_category = current_category.gifs.all()
    print(gif_in_category)
    
    context ={'gifs': gif_in_category,
              'category': current_category}
    
    return render(request, 'gifsincategory.html', context)

def categories_list(request):
    # Categories view: this view will display all the existing categories from the database. 
    # Each category has a link redirecting the user to the Category view.
    
    category_list = Category.objects.all() #get category 
        
    context ={'categories': category_list}
    
    return render(request, 'allcategories.html', context)


def gif_id(request, id : int):
# Gif view: this views accepts a gif id and display that specific gifs details on the page. 
# Display each gif in an img tag

    gif_id = Gif.objects.get(id = id) #get gif bt id
    category_list = gif_id.categories.all() ## Get the categories of one as example  q1.category_set.all()
    print(gif_id)
    # print(category_list)
    context ={'gif': gif_id,
              'category': category_list}
    
    return render(request, 'gif_view.html', context)