# Faça um programa que receba dois números inteiros.
# e gere os números inteiros que estão no intervalo compreendido por eles
while True:
    n1 = int(input('Digite: '))
    n2 = int(input('Digite: '))
    for c in range(n1, n2):
        print(f'{c}')
    usuario = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if usuario == 'N':
        break
print('FIM DO PROGRAMA')
