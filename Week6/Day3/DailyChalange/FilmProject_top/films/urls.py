from django.contrib import admin
from django.urls import path
from .views import (HomePageView,
                         FilmCreateView,
                         DirectorCreateView,
                         FilmDeleteView,
                         conf_delete,
                         FavoriteFilmView,
                         FilmDetailView,
                         manage_producers
                        #  AddFavouriteFilmView,
                        #  DeleteFavouriteFilmView
                         
                        )       

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name = 'homepage'),
    path('addfilm/', FilmCreateView.as_view(), name = 'addfilm'),
    path('adddirector/', DirectorCreateView.as_view(), name = 'adddirector'),
    path('deletefilm/<int:pk>', FilmDeleteView.as_view(), name = 'deletefilm'),
    path('confdelete/', conf_delete, name = 'confirm_delete'),
    # path('filmdetails/', conf_delete, name = 'confirm_delete'),
    # path('filmfavourite-add/<int:pk>', AddFavouriteFilmView.as_view(), name = 'film_favourite_add'),
    # path('filmfavourite-delete/<int:pk>', DeleteFavouriteFilmView.as_view(), name = 'film_favourite_delete'),
    path('homepage/favorites/<int:film_id>', FavoriteFilmView.as_view(), name = 'favorites'),
    path('homepage/details/<int:pk>', FilmDetailView.as_view(), name = 'details'),
    path('manage-producers/', manage_producers, name = "manage_producers"),
]