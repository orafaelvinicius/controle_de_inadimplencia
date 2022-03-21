from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inadimplentes/templates/<int:inquilino_id>', views.pageinquilino, name='pageinquilino'),
    path('busca', views.buscar, name='buscar'),
    path('usuarios', views.inquilinos, name='usuarios'),  
]