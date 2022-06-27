while True:
    base = int(input('Base: '))
    expoente = int(input('Expoente: '))
    resp = base ** expoente
    print(resp)
    usuario = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if usuario == 'N':
        break
print('FIM DO PROGRAMA')
