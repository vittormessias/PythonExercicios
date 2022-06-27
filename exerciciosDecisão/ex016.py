a = int(input('Digite um valor: '))
if a == 0:
    print('Não é uma equação do segundo grau!')
    exit()
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
delta = (b ** 2) - (4 * a * c)
if delta < 0:
    print('A equação não possui raizes: {}'.format(delta))
    exit()
elif delta == 0:
    print('Possui apenas uma raiz real: {}'.format(delta))
elif delta > 0:
    print('A equação possui duas raizes reais: {}'.format(delta))

