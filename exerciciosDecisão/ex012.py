hora = float(input('Digite o valor da sua hora: '))
mes = int(input('Digite a quantidade de horas trabalhadas no mês: '))
salario = hora * mes
IR = []
if 900 >= salario:
    IR = 0
elif salario <= 1500:
    IR = 5
elif salario <= 2500:
    IR = 10
elif salario > 2500:
    IR = 20
print('-=' * 20)
print('Salario bruto:              {:.2f}'.format(salario))
print('(-) IR {}%                  {:.2f}'.format(IR, salario * IR / 100))
print('(-) INSS (10%)              {:.2f}'.format(salario * 10 / 100))
print('FGTS (11%)                  {:.2f}'.format(salario * 11 / 100))
print('Total de descontos:         {:.2f}'.format(salario * (IR + 10) / 100))
print(f'Salario liquido:            {(salario - (salario * (IR + 10) / 100)):.2f}')
print('=-' * 20)

