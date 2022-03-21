from pyexpat import model
from re import search
from django.contrib import admin
from .models import Inquilino

class ListandoInquilinos(admin.ModelAdmin):
    list_display = (
        'id', 
        'nome', 
        'status_de_pagamentos', 
        'tamanho_do_kitnet', 
        'valor_do_aluguel',
        'ultimo_pagamento',
    )
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter = ('status_de_pagamentos',)
    list_per_page = 10



admin.site.register(Inquilino, ListandoInquilinos)


