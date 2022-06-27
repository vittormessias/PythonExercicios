lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    usuario = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if usuario == 'N':
        break
    if usuario not in 'S':
        usuario = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
print(f'Foram digitados {len(lista)} numeros')

print(lista.sort(reverse=True))

if 5 in lista:
    print('Valor 5 está na lista')
else:
    print('Valor 5 não está na lista')

