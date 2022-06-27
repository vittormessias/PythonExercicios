from time import sleep
print('     Super Gerador de PA')
print('=-'*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
mais = 10
novoTermo = 1
while novoTermo != 0:
    mais += novoTermo
    while cont <= mais:
        print('{}'.format(termo), end='-> ')
        termo += razao
        cont +=1
    print('PAUSA')
    novoTermo = int(input('Mais quantos termos? '))
print('Saindo..')
sleep(2)
print('Fim do Programa')
