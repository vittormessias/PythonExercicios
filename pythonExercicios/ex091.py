from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }
ranking = dict()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f' {k} com {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(' == Ranking dos jogadores == ')
for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
print(jogo)
'''lista = []

jogada1 = {'jogador1': randint(1, 6)}
jogada2 = {'jogador2': randint(1, 6)}
jogada3 = {'jogador3': randint(1, 6)}
jogada4 = {'jogador4': randint(1, 6)}

lista.append([jogada1.copy(), jogada2.copy(), jogada3.copy(), jogada4.copy()])

print('Valores sorteados: ')
print(f'    O jogador1 tirou {lista[0][0]["jogador1"]}')
sleep(1)
print(f'    O jogador2 tirou {lista[0][1]["jogador2"]}')
sleep(1)
print(f'    O jogador3 tirou {lista[0][2]["jogador3"]}')
sleep(1)
print(f'    O jogador4 tirou {lista[0][3]["jogador4"]}')
sleep(1)

print(lista)
print('Ranking dos jogadores: ')
for i in lista[0]:
    for k, v in i.items():
        print(f'     1° lugar: {k} com {v}')
        print(f'     2° lugar: {k} com {v}')
        print(f'     3° lugar: {k} com {v}')
        print(f'     4° lugar: {k} com {v}')'''







