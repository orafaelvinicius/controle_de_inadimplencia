from datetime import date
from django.db import models

kitnet = (
    ('Pequeno', 'Pequeno'),
    ('Medio', 'Medio'),
    ('Grande', 'Grande'),
)

status_adimplencia = (
    ('ADIMPLENTE', 'ADIMPLENTE'),
    ('INADIMPLENTE', 'INADIMPLENTE')
)

class Inquilino(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15, unique=True)
    tamanho_do_kitnet = models.CharField(max_length=10, choices=kitnet)
    status_de_pagamentos = models.CharField(max_length=15, choices=status_adimplencia, default='ADIMPLENTE')
    valor_do_aluguel = models.CharField(max_length=255)
    ultimo_pagamento = models.DateField(blank=True) # Usar para a função que define a inadimplencia
    

    def __str__(self):
        return self.nome