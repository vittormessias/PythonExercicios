# Faça um programa que leia 5 números e informe o maior número.
for c in range(1, 6):
    n1 = int(input('Digite o {}° numero: '.format(c)))
    if c == 1 or maior < n1:
        maior = n1
print(maior)
