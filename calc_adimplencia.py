from datetime import datetime
from dateutil.relativedelta import relativedelta

ultimo_pagamento = datetime(2021, 3, 2) # Ajustar input
data_do_pagamento = datetime.now()

diff = relativedelta(data_do_pagamento, ultimo_pagamento)

# Imprimindo apenas diferenças menores de 1 ano
if diff.months >= 1 or diff.years > 0:
    print(f'INADIMPLENTE a {diff.years} anos e {diff.months} meses!')
else:
    print(f"Está ADIMPLENTE. Último pagamento aconteceu a {diff.days} dias atrás")

