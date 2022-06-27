'''oposto = float(input('Digite um valor do cateto oposto: '))
adjacente = float(input('Digite um valor do catteto adjacente: '))
valorFinal = oposto + adjacente
print('O valor da hipotenusa é {}'.format_map(valorFinal))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

