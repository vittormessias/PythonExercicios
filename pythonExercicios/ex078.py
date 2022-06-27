lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
print(f'Você digitou os valores {lista}')
print('O maior valor foi ', max(lista), 'na posição ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print()
print('O menor valor foi ', min(lista), 'na posição ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
print()


# Solução antiga
'''lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('=' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()'''




