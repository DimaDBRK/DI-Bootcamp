"""
URL configuration for xp_d4 project.

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
from todo.views import add_todo_view, display_todos, done_todo_view, add_category_view, display_todos_v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_todo/', add_todo_view),
    path('add_category/', add_category_view),
    path('display_todos_v2/', display_todos_v2),
    path('display_todos/', display_todos),
    path('display_todos/<int:id>', done_todo_view),
    # path('done/', done_todo_view)
    
]
