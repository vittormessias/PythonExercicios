n1 = int(input('\033[31mDigite um numero: \033[m'))
n2 = int(input('\033[36mDigite outro numero: \033[m'))
if n1 > n2:
    print('\033[31mO primeiro valor é maior\033[m')
elif n1 < n2:
    print('\033[36mO segundo valor é maior\033[m')
else:
    print('Não existe valor maior, os dois são iguais.')
