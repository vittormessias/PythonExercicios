from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO maior numero sorteado foi {max(tupla)}')
print(f'O menor numero sorteado foi: {min(tupla)}')

# resolução antiga
'''for c in range(1, 6):
    # Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
    tupla = (randint(1, 10))
    # Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
    print(f'Os valores sorteados foram: {tupla}')
    if c == 1:
        menor = tupla
        maior = tupla
    else:
        if tupla > maior:
            maior = tupla
        if tupla < menor:
            menor = tupla
print(f'O maior numero sorteado foi {maior}\n'
      f'O menor numero sorteado foi: {menor}')'''
