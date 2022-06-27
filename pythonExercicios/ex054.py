# Crie um programa que leia o ano de nascimento de sete pessoas.
from datetime import date
anoAtual = date.today().year
maior = 0  # Contador
menor = 0  # Contador
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = anoAtual - nascimento
    # No final, mostre quantas pessoas ainda não atingiram a maioridade
    # e quantas já são maiores.
    if idade >= 18:
        maior += 1  # Contador
    else:
        menor += 1  # Contador
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))

