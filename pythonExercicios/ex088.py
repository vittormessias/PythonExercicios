from random import randint
from time import sleep
megaSena = []
jogos = []
print('='*30)
print('         MEGA SENA    ')
print('='*30)
quantidadeJogos = int(input('Quantos jogos você quer que eu sorteie? '))
totalJogos = 0
while totalJogos < quantidadeJogos:
    cont = 1
    while True:
        numero = randint(1, 60)
        if numero not in megaSena:
            megaSena.append(numero)
            cont += 1
        if cont >= 6:
            break
    megaSena.sort()
    jogos.append(megaSena[:])
    megaSena.clear()
    totalJogos += 1
print('-=' * 3, f' SORTEANDO {quantidadeJogos} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)







