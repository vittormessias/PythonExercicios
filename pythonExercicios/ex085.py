numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° numero: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    if valor % 2 == 1:
        numeros[1].append(valor)
print('-=' * 30)

numeros[0].sort()
print('Par: ', end='')
print(numeros[0])

numeros[1].sort()
print(f'Impar: ', end='')
print(numeros[1])
