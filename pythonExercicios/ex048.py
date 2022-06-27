# Soma ímpares múltiplos de três
soma = 0  # Atribuição
cont = 0  # Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma = soma + c
print('A soma de {} valores é {}'.format(cont, soma))

