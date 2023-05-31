"""
URL configuration for giphy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gifs.views import add_new_gif, add_new_category, all_gifs, category_info, categories_list, gif_id, add_from_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gifs/', add_new_gif), 
    path('categories/', add_new_category),
    path('homepage/', all_gifs),
    path('categorygif/', categories_list),
    path('categorygif/<int:id>', category_info, name = 'details'), #
    path('gif/<int:id>', gif_id), #forgif id
     path('addfromapi/', add_from_api), #forgif id
]
