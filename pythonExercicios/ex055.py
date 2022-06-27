# Faça um programa que leia o peso de cinco pessoas.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o {}° peso: '.format(p)))
    # No final, mostre qual foi o maior e o menor peso lidos.
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('E o menor peso é {}'.format(menor))
