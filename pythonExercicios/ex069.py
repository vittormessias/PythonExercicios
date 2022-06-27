contIdade = contHomem = contMulher = cont = 0
while True:
    print('-='*15)
    print('CADASTRE UMA PESSOA')
    print('-=' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        contIdade += 1
    if sexo == 'M':
        contHomem += 1
    if sexo == 'F' and idade < 20:
        contMulher += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
print('-='*15)
print('Fim do programa!')
print(f'\033[32m{contIdade}\033[m pessoas tem mais de 18 anos.\n'
      f'\033[36m{contHomem}\033[m homens foram cadastrados.\n'
      f'\033[34m{contMulher}\033[m mulheres tem menos de 20 anos.')
print('-='*15)
