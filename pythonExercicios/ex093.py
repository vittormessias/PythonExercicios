jogador = dict()
paridas = []
jogador['nome'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total):
    paridas.append(int(input(f'  Quantos gols na partida {c}? ')))
jogador['gols'] = paridas[:]
jogador['total'] = sum(paridas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

# ----------------------------------------------------------------------------------------------------------------------
# Solução Antiga
'''jogador = dict()
lista = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = lista[:]
    total = 0
    for v in lista:
        total += v
        jogador['total'] = total
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for c, v in enumerate(lista):
    print(f'    => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')'''
