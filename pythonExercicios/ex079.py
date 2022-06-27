lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        usuario = str(input('Valor adicionado. Deseja continuar? [S/N]')).strip().upper()[0]
    else:
        print('Valor duplicado! Não vou adicionar...')
        usuario = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if usuario == 'N':
        break
    else:
        if usuario not in 'S':
            usuario = str(input('Valor invalido. Deseja continuar? [S/N]')).strip().upper()[0]
lista.sort()
print(lista)
