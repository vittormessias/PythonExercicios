salario = float(input('Digite um salario: '))
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))

#solução antiga
'''if salario > 1250:
    novoSalario = salario + (salario * 10 / 100)
    print('Com o aumento de 10% o novo salario é de {:.3f}'.format(novoSalario))
else:
    novoSalario = salario + (salario * 15 / 100)
    print('Com o aumento de 15% o novo salario é de {:.3fs}'.format(novoSalario))'''
