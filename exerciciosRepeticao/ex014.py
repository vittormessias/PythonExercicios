impar = par = 0
for c in range(1, 11):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par += 1
    if n % 2 == 1:
        impar += 1
print(f'Impar {impar} e Par {par}')
