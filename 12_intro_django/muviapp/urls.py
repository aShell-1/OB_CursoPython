from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_peliculas, name='url_peliculas'),
    path('directores/', views.directores, name='url_directores'),
    path('peliculas/<peli_id>', views.peliporid, name='url_peliporid')
]