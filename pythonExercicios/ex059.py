# Criando um Menu de Opções
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do Programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente!')
    print('=-'*20)
    sleep(2)
print('Fim do programa! Volte sempre!')

# Solução Antiga
'''valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um outro valor: '))
menu = 0
while menu != 5:
    menu = int(input('[1] Somar\n'
                     '[2] Multiplicar\n'
                     '[3] Maior\n'
                     '[4] Novos numeros\n'
                     '[5] Sair do Programa\n'
                     ':'))
    if menu == 1:
        soma = valor1 + valor2
        print('A soma dos valores {} e {} é {}'.format(valor1, valor2, soma))
    elif menu == 2:
        multiplicar = valor1 * valor2
        print('Os valores {} x {} é {}'.format(valor1, valor2, multiplicar))
    elif menu == 3:
        if valor1 > valor2:
            print('Maior', valor1)
        else:
            print('Maior', valor2)
    elif menu == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite um outro valor: '))
print('Acabou')'''
