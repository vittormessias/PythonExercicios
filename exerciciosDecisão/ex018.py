from datetime import datetime
data = input('Digite uma data em formato [dd/mm/yy]: ')
datetime.strptime(data, '%d/%m/%y').date()
if data == data:
    print(data)
else:
    print('Inválido')

