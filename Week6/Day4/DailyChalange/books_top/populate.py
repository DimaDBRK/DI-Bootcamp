import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.settings')
import django
import random
import datetime

import requests
import os
import json
import urllib.request
from urllib import parse, request

django.setup()

from review.models import Book
from faker import Faker

def add_book():
    url = "https://www.googleapis.com/books/v1/volumes?q=test"
    category = ['fun','cook', 'smile','sport','sleep','eat','drive','learn','duck','dog']
    # qty_in_req = 2
    # author = 'API'
    for categ in category:
        params = parse.urlencode({
        "q": categ,
        })

        try:
            with urllib.request.urlopen("".join((url, "?", params))) as response:
                data = json.loads(response.read())

    
            if response.status == 200:
                print('OK')
                print(categ, '- -', data['totalItems'])
                print(len(data['items']))
                for item in data['items']:
                    if ('categories' in item['volumeInfo'] and 
                        'imageLinks' in item['volumeInfo'] and  
                        'description' in item['volumeInfo'] and  
                        'pageCount' in item['volumeInfo'] and 
                        'authors' in item['volumeInfo'] and 
                        len(item['volumeInfo']['title']) <= 50):
                        
                        title_new = item['volumeInfo']['title']
                        author_new = item['volumeInfo']['authors'][0]
                        publish_date_new = item['volumeInfo']['publishedDate']
                        description_new = item['volumeInfo']['description'][:89]
                        page_count_new = item['volumeInfo']['pageCount']
                        categories_new = item['volumeInfo']['categories'][0]
                        thumbnail_url_new = item['volumeInfo']['imageLinks']['smallThumbnail']
                        
                        # format
                        if len(publish_date_new) <= 4:
                                publish_date_new += '-01-01'
                        elif len(publish_date_new) <= 7 and len(publish_date_new) > 4:
                                publish_date_new += '-01'
                        
                        
                        print(title_new)
                        print(author_new)
                        print(publish_date_new)
                        print(description_new)
                        print(page_count_new)
                        print(categories_new)
                        print(thumbnail_url_new)
                       
                        
                        book = Book(title = title_new,
                                    author = author_new,
                                    publish_date = publish_date_new,
                                    description = description_new, 
                                    page_count = page_count_new,
                                    categories = categories_new,
                                    thumbnail_url = thumbnail_url_new)
                        
                        book.save()
                    
                    else:
                        pass
                
              
                    
                    # title_res = item["title"] if len(item["title"]) >=1 else "No info"
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")    

# add_book()
