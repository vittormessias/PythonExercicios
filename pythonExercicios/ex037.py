numero = int(input('Escreva um numero: '))
base = int(input('Qual será a base de conversão? \n'
                 '1 - Binario \n'
                 '2 - Octal \n'
                 '3 - hexadecimal \n'
                 ': '))
if base == 1:
    numero = bin(numero)[2:]
    print(numero)
elif base == 2:
    numero = oct(numero)[2:]
    print(numero)
elif base == 3:
    numero = hex(numero)[2:]
    print(numero)
else:
    print('opção invalida!')