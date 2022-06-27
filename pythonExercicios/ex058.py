# Jogo da adivinhação
from random import randint
computador = randint(0, 10)
print('Sou seu computador... acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. tente mais uma vez.')
        elif jogador > computador:
            print('Menos.. tente mais uma vez.')
print('Você acertou com {} tentativas. Parabéns!'.format(palpites))

# Solução Antiga
'''from random import randint
from time import sleep
usuario = ''
computador = randint(0, 10)
cont = 0
while usuario != computador:
    print('Sou seu computador...\n'
          'Acabei de pensar em um numero entre 0 e 10. \n'
          'Será que você consegue advinhar qual foi?')
    usuario = int(input('Qual é o seu palpite? '))
    print('Processando...')
    sleep(2)
    print('Você errou!')
    cont += 1
print('Processando...')
sleep(2)
print('Parabens você acertou! Precisou de {} palpites para vencer!'.format(cont))'''
