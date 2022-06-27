# Numeros primos
n = int(input('Digite um numero: '))
total = 0  # Contador
for c in range(1, n + 1):
    if n % c == 0:  # Formula
        print('\033[32m{}\033[m'.format(c), end=' ')
        total += 1  # Contador
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
print('\nO numero {} foi divisível {} vezes'.format(n, total))
if total == 2:  # Contador
    print('PRIMO!')
else:
    print('Não é PRIMO!')
