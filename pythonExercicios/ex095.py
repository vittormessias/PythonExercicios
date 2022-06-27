jogador = dict()
partidas = []
lista = []
while True:
    partidas.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, total):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    lista.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! Não existe jogador com esse código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}:')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE! >>')



# Código antigo
'''jogador = dict()
partidas = []
lista = []
while True:
    partidas.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, total):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    lista.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod nome      gols         total')
print('-' * 33)
for k, v in enumerate(lista):
    print(f'{k:2}  {v["nome"]}    {v["gols"]}    {v["total"]}')
print('-' * 33)
mostrarValor = int(input('Mostar dados de qual jogador? (999 para parar) '))
for k, v in enumerate(lista):
    if k == mostrarValor:
        print(f'-- LEVANTAMENTO DO JOGADOR {v["nome"]}: ')
        for p, g in enumerate(v["gols"]):
            print(f'    Na partida {p+1} fez {g} gols.')'''
