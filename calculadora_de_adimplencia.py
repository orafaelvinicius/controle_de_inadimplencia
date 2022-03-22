from datetime import datetime
from dateutil.relativedelta import relativedelta

ultimo_pagamento = datetime(2021,2,1,23)
data_do_pagamento = datetime.now()


diff = relativedelta(data_do_pagamento, ultimo_pagamento)

# Imprimindo apenas diferenças menores de 1 ano
if diff.months >= 1 and diff.years > 0:
    print(f'Você está devendo {diff.months} meses ou mais de aluguel. Seu status é de INADIMPLENTE!')
else:
    print(f"Você está ADIMPLENTE. Seu último pagamento aconteceu a {diff.days} dias atrás")
