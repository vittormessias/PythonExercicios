cont = soma = 0
numero = int(input('Digite um numero: '))
while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite um numero: '))
print('Foram digitados {} numeros e a soma entre eles é {}'.format(cont, soma))
