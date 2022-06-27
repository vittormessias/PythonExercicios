n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
operacao = int(input('Qual operação deseja fazer? par ou impar = 1 / positvo ou negativo = 2 / inteiro ou decimal = 3: '))
if operacao == 1:
    if int(n1 + n2) % 2 == 0:
        print('A operação escolhida foi Par ou Impar. O resultado da escolha dos numeros foi: Par')
    else:
        print('A operação escolhida foi Par ou Impar. O resultado da escolha dos numeros foi: Impar')
elif operacao == 2:
    if int(n1 - n2) > 0:
        print('A operação escolhida foi Positivo ou Negativo. O resultado da escolha dos numeros foram: Positivo {}'.format(n1 - n2))
    else:
        print('A operação escolhida foi Positivo ou Negativo. O resultado da escolha dos numeros foram: Negativo {}'.format(n1 + n2))
elif operacao == 3:
    final = n1 + n2
    if final == round(final):
        print('A operação escolhida foi Inteiro ou Decimal. O resultado da escolha dos numeros foram: Inteiro {} '.format(round(final)))
    else:
        print('A operação escolhida foi Inteiro ou Decimal. O resultado da escolha dos numeros foram: Decimal {}'.format(round(final)))
