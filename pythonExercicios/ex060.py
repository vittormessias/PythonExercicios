# Cálculo do fatorial
from math import factorial
print('Digite um numero para ')
n = int(input('Calcular seu fatorial: '))
f = factorial(n)
print('{}'.format(f))

# Solução com for
'''print('Digite um numero para ')
n = int(input('Calcular seu fatorial: '))
f = 1
for c in range(n, 1, - 1):
    f *= c
print('{}'.format(f))'''

# Solução Antiga
'''print('Digite um numero para ')
n = int(input('Calcular seu fatorial: '))
cont = n
f = 1
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))'''
