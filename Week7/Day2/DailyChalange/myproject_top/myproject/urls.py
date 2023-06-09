"""
URL configuration for myproject project.

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
from apptask.views import DepartmentListView, EmployeeListView, TaskListView, ProjectListView, ProjectDetailView, TaskDetailView, DepartmentDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/departments/', DepartmentListView.as_view(), name = 'departments'),
    path('api/employees/', EmployeeListView.as_view(), name = 'employees'),
    path('api/projects/', ProjectListView.as_view(), name = 'projects'),
    path('api/tasks/', TaskListView.as_view(), name = 'tasks'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name = 'project-detail' ),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name = 'task-detail' ),
    path('api/departments/<int:pk>/', DepartmentDetailView.as_view(), name = 'department-detail'),
    # path('api/department-create/', DepartmentCreateAPIView.as_view(), name = 'department-create'),
]

