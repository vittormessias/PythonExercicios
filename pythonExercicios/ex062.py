# Super Progressão Aritmética
print('     Super Gerador de PA')
print('=-'*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
novoTermo = 10
while novoTermo != 0:
    total += novoTermo
    while cont <= total:
        print('{}'.format(termo), end='-> ')
        termo += razao
        cont += 1
    print('PAUSA')
    novoTermo = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM DO PROGRAMA COM {} TERMOS REALIZADOS'.format(total))






