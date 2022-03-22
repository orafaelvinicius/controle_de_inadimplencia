from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:inquilino_id>', views.pageinquilino, name='pageinquilino'),
    path('busca', views.buscar, name='buscar'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('inquilinos', views.inquilinos, name='inquilinos'),
    path('cria_inquilino', views.cria_inquilino, name='cria_inquilino'),
]