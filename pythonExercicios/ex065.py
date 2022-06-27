usuario = 'S'
maior = 0
menor = 0
cont = 0
soma = 0
while usuario in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    usuario = str(input('Sim\n'
                        'Não\n'
                        'Deseja continuar? ')).upper().strip()[0]
    if cont == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print('A media entre todos os valores é {}\n'
      'E o maior valor é {} e o menor é {}'.format(media, maior, menor))


