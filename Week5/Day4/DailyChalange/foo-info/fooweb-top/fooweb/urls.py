"""
URL configuration for fooweb project.

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
from info.views import phone_sh
from info.views import name_sh,  search_phone


urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/<int:phone_number>', phone_sh, name = 'phone'), #for search by phone
    path('persons/<str:name>', name_sh, name = 'name'), #for search by name
    # path('persons-search/', search_by, name= 'search_by'),
    path('search/', search_phone, name='search'), #v2
]
