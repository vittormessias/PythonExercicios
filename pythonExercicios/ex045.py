from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura' )
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra 
[1] Papel
[2] Tesoura''')
jogador = int(input('Sua jogada é: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {} '.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('=-'*11)
if computador == 0: #Pedra
    if jogador == 0: #Jogador Pedra
        print('Empate')
    elif jogador == 1: #Jogador Papel
        print('jOgador Venceu')
    elif jogador == 2: #jogador Tesoura
        print('Computador Venceu!')
    else:
        print('Jogada Invalida')

elif computador == 1: #Papel
    if jogador == 0: #Jogador Pedra
        print('Computador Venceu!')
    elif jogador == 1: #Jogador Papel
        print('EMPATE')
    elif jogador == 2: #jogador Tesoura
        print('JOGADOR VENCEU!')
    else:
        print('Jogada Invalida')
elif computador == 2: #Tesoura
    if jogador == 0: #Jogador Pedra
        print('Jogador venceu!')
    elif jogador == 1: #Jogador Papel
        print('Computador venceu!')
    elif jogador == 2: #jogador Tesoura
        print('EMPATE')
    else:
        print('Jogada Invalida')


'''Código Antigo'''
'''import random
print('=-'*20)
numero = int(input('Vamos jogar jokenpô? \n'
                   '2 - \033[36mTesoura\033[m\n'
                   '5 - Papel\n'
                   '0 - \033[34mPedra\033[m\n'
                   'Digite um numero: '))
print('=-'*20)
escolha = [0, 2, 5]
computador = random.choice(escolha)
if numero == computador:
    print('Empate!')
elif numero == 2 and computador != 0 or numero == 5 and computador != 2 or numero == 0 and computador != 5:
    print('Você ganhou! O computador escolheu {}'.format(computador))
else:
    print('O computador \033[33mganhou!\033[m O computador escolheu \033[4m{}\033[m'.format(computador))
'''
