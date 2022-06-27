saque = float(input('Digite o valor do saque R$: '))
cem = int(saque / 100)
saque = saque % 100
cinquenta = int(saque / 50)
saque = saque % 50
dez = int(saque / 10)
saque = saque % 10
cinco = int(saque / 5)
saque = saque % 5
um = saque
print('Notas de cem {}, Notas de cinquenta {}, Notas de dez {}, Notas de cinco {} e Notas de um {:.0f}'.format(cem, cinquenta, dez, cinco, um))

