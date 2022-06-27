from datetime import date
anoNascimento = int(input('Digite o seu ano de nascimento: '))
anoAtual = date.today().year
dataFinal = anoAtual - anoNascimento
if dataFinal < 18:
    falta = 18 - dataFinal
    print('Você tem {} anos, vai ter que se alistar! Faltam {} anos!'.format(dataFinal, falta))
    anoAlistamento = anoAtual + falta
    print('Seu alistamento vai ser em {}'.format(anoAlistamento))
elif dataFinal == 18:
    print('Está na hora de se alistar! Você tem {} anos!'.format(dataFinal))
elif dataFinal > 18:
    falta = dataFinal - 18
    print('Já passou do tempo de se alistar! Você tem {} anos. Já se passaram {} anos'.format(dataFinal, falta))
    anoAlistamento = anoAtual - falta
    print('Seu alistamento foi em {}'.format(anoAlistamento))


