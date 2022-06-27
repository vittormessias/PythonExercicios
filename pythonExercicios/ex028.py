from random import randint
from time import sleep
usuario = int(input('Qual foi o numero escolhido pelo computador?'))
computador = randint(0, 5)
print('Processando...')
sleep(3)
if computador == usuario:
    print('Parabéns, você acertou!')
else:
    print('Você errou! O numero que o computador escolheu foi {}'.format(computador))
