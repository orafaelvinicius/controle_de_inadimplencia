from django.db import models
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

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
    valor_do_aluguel = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    ultimo_pagamento = models.DateField(blank=True) 
    inadimplencia = models.CharField(max_length=255, default='0')

    def __str__(self):
        return self.nome

    @property
    def calcula_inadimplencia(self):
        ultimo_pagamento = self.ultimo_pagamento
        data_de_hoje = datetime.now()

        diff = relativedelta(data_de_hoje, ultimo_pagamento)

        if diff.months >= 1 or diff.years > 0:
            self.inadimplencia = diff.months

            return self.inadimplencia
        else:
            self.inadimplencia = '0'
            return self.inadimplencia
            
    def percentual_inadimplencia(self):
        total_inquilinos = 100
        total_inadimplentes = 30 

        percentual_inadimplentes  = int((total_inadimplentes / total_inquilinos ) * 100)

        print(f'Atualmente o percentual de inadimplentes é de {percentual_inadimplentes} %')
