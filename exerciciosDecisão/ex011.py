salario = float(input('Qual é o seu salario em R$: '))
if salario <= 280:
    porcentual = 20
    novoSalario = salario + (salario * 20 / 100)
elif 280 <= salario <= 700:
    porcentual = 15
    novoSalario = salario + (salario * 15 / 100)
elif 700 <= salario <= 1500:
    porcentual = 10
    novoSalario = salario + (salario * 10 / 100)
elif salario >= 1500:
    porcentual = 5
    novoSalario = salario + (salario * 5/ 100)
print('O seu salario atual é R${:.2f}, com um incremente de {}% passa a ser R${:.2f}'.format(salario, porcentual, novoSalario))

