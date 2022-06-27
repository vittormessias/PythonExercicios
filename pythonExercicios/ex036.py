casa = float(input('Qual é o valor da casa: R$ '))
salario = float(input('Qual é o seu salario: R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)
porcentagemSalario = salario * 30 / 100
if prestacao >= porcentagemSalario:
    print('Para pagar  uma casa de {:.2f} em {} anos a prestação será de {:.2f}. Emprestimo negado!'.format(casa, anos, prestacao))
elif prestacao < porcentagemSalario:
    print('Para pagar  uma casa de {:.2f} em {} anos a prestação será de {:.2f}. Emprestimo aceito!'.format(casa, anos, prestacao))


