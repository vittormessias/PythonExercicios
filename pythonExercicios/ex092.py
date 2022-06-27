from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
anoNasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = anoAtual = datetime.now().year - anoNasc
trabalhador['cpts'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['cpts'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratacao'] + 35) - datetime.now().year)
print('-='*30)
for k, v in trabalhador.items():
    print(f'  - {k} tem o valor {v}')

