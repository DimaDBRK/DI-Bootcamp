from django.urls import path

from .views import SignUpView, LoginPageView, logoutView



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logoutView, name = 'logout'),
]

