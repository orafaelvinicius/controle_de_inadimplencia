from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('inquilinos', views.inquilinos, name='inquilinos'),
    path('cria_inquilino', views.cria_inquilino, name='cria_inquilino'),
    path('deleta_inquilino/<int:inquilino_id>', views.deleta_inquilino, name='deleta_inquilino'),
    path('edita_inquilino/<int:inquilino_id>', views.edita_inquilino, name='edita_inquilino'),
    path('atualiza_inquilino/<int:inquilino_id>', views.atualiza_inquilino, name='atualiza_inquilino'),
    path('buscar', views.percentual_inadimplencia, name='percentual_inadimplencia'),
]