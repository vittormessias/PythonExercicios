from random import randint
cont = 0
while True:
    print('-=' * 15)
    print('VAMOS JOGAR PAR OU IMPAR? ')
    print('-=' * 15)
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('[P/I]\n'
                         'Par ou Impar?')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total foi {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            cont += 1
            print('Você Venceu!')
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            cont += 1
            print('Você Venceu!')
        else:
            print('Você Perdeu!')
            break
    print('Vamos Jogar novamente..')
print(f'O total de vitórias consecutivas foi {cont}')
