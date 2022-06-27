listaTemporaria = []
lista = []
maior = menor = 0
while True:
    listaTemporaria.append(str(input('Nome: ')))
    listaTemporaria.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = listaTemporaria[1]
    else:
        if listaTemporaria[1] > maior:
            maior = listaTemporaria[1]
        if listaTemporaria[1] < menor:
            menor = listaTemporaria[1]
    lista.append(listaTemporaria[:])
    listaTemporaria.clear()
    usuario = str(input('Deseja continuar? [S/N]'))[0]
    if usuario in 'Nn':
        break
    if usuario not in 'Ss':
        print('valor inválido..')
        usuario = str(input('Deseja continuar? [S/N]'))[0]
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maior} kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()  # print vazio para pular uma linha
print(f'O menor peso foi de {menor} kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')


"""---------------------------------------------------------------------------------------------------------------------"""
'''pessoas = list()
dado = list()
cont = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    usuario = str(input('Deseja continuar? [S/N]')).strip()[0].upper()
    cont += 1

    if usuario in 'Nn':
        break
    if usuario not in 'S':
        print('valor inválido..')
        usuario = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

print(f'Foram cadastradas {cont} pessoas')

for p in pessoas:
    if p[1] > 70:
        print(f'O maior peso foi {p[1]}. Peso de ', end='')
        print(p[0])
    else:
        print(f'O menor peso foi {p[1]}. Peso de ', end='')
        print(p[0])'''

