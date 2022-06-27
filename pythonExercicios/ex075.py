# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
# A) Quantas vezes apareceu o valor 9.
print(f'O numero 9 apareceu {tupla.count(9)} vezes.')
# B) Em que posição foi digitado o primeiro valor 3.
if 3 in tupla:
    print(f'O valor 3 foi digitado na posição {tupla.index(3)+1}')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')
# C) Quais foram os números pares.
print(f'Os numeros pares foram', end=' ')
for numero in tupla:
    if numero % 2 == 0:
        print(f'{numero}', end=' ')
