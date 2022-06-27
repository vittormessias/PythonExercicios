from datetime import date
anoNascimento = int(input('Digite um ano de nascimento: '))
anoAtual = date.today().year
anoFinal = anoAtual - anoNascimento
if anoFinal <= 9:
    print('Você tem {} anos, MIRIM!'.format(anoFinal))
elif anoFinal <= 14:
    print('Você tem {} anos, INFANTIL!'.format(anoFinal))
elif anoFinal <= 19:
    print('Você tem {} anos, JUNIOR!'.format(anoFinal))
elif anoFinal <= 25:
    print('Você tem {} anos, SÊNIOR!'.format(anoFinal))
else:
    print('Você tem {} anos, MASTER!'.format(anoFinal))
