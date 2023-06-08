"""
URL configuration for Image_sharing project.

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
from django.contrib.auth import views
from image_share.views import RegisterView, HomePageView, profile, AddImageView, MyImagesView

from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('homepage/', HomePageView.as_view(), name = 'homepage'),
    path('profile/<int:id>/', profile, name = 'profile'),
    path('upload-image', AddImageView.as_view(), name = 'upload'),
    path('my-images/', MyImagesView.as_view(), name='my_images'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new