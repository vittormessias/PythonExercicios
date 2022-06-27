print('"M" para Matutino ou "V" para Vespertino ou "N" para Noturno')
turno = str(input('Em qual turno você estuda?')).upper()
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
