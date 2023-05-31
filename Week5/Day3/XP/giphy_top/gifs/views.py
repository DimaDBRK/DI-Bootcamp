from django.shortcuts import render
import psycopg2
from .models import Gif, Category
from .forms import GifForm, CategoryForm
import requests
import os
import json
import urllib.request
from urllib import parse, request

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

# XP Gold update urls
def add_from_api(request):
    url = "http://api.giphy.com/v1/gifs/search"
    category = ['fun','cook', 'smile','sport','sleep','eat','drive','learn','duck','dog']
    qty_in_req = 10
    author = 'API'
    for categ in category:
        params = parse.urlencode({
        "q": categ,
        "api_key": "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My",
        "limit": qty_in_req,
        "rating": "g" # 
        })

        try:
            with urllib.request.urlopen("".join((url, "?", params))) as response:
                data = json.loads(response.read())

    
            if response.status == 200:
                for item in data['data']:
                    title_res = item["title"] if len(item["title"]) >=1 else "No info"
                    url_res = item["images"]["fixed_height"]["url"].split("?")[0]
                    url_res = url_res if '.gif' in url_res else "https://no.url"
                
                # Insert in the database
                if url_res != "https://no.url":
                    Gif.objects.create(title = title_res, url = url_res, uploader_name = author)
                                     
            else:
                print(f"Error:")
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            
            #    Getting all the stuff from database
        query_results = Gif.objects.filter(uploader_name = 'API')

                    # Creating a dictionary to pass as an argument
        context = { 'query_results' : query_results }
        
    return render(request, 'addfromapi.html', context)