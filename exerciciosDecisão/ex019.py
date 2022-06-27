numero = int(input('Digite um numero inteiro menor do que 1000: '))
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10
if 1000 <= numero:
    print('Inválido')
elif 1000 >= centena >= 99 and centena != 0:
    centena = centena
elif 99 >= dezena >= 10:
    dezena = dezena
elif 9 >= unidade >= 0:
    unidade = unidade
print(centena, dezena, unidade)
