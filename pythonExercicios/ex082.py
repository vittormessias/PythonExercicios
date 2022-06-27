lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    usuario = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if usuario == 'N':
        break
    if usuario not in 'S':
        usuario = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    for c in range(0, len(lista)):
        if c % 2 == 0:
            par = (lista[c])
        if c % 2 == 1:
            impar = (lista[c])
print(f'Par: {par}')
print(f'Impar: {impar}')
