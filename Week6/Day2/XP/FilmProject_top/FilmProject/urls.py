"""
URL configuration for FilmProject project.

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
from django.urls import path, include
# from films.views import (HomePageView,
#                          FilmCreateView,
#                          DirectorCreateView
#                         )       

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('homepage/', HomePageView.as_view(), name = 'homepage'),
#     path('addfilm/', FilmCreateView.as_view(), name = 'addfilm'),
#     path('adddirector/', DirectorCreateView.as_view(), name = 'adddirector'),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include('films.urls')), #include urls from other application
    path('accounts/', include('accounts.urls')) #include urls from other application
    
]