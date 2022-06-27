# Faça um programa que leia 5 números
s = 0
for c in range(1, 6):
    print('---- {}° Numero -------'.format(c))
    n = int(input('Numero: '))
    # e informe a soma
    s += n
# e a média dos números.
n = s / 5
print('A soma é {} e a media é {}'.format(s, n))
