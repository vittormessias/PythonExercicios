n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1 + n2) / 2
print('-='*20)
print('Media de Aproveitamento: {} / Conceito / Situação'.format(media))
if 9.0 <= media <= 10.0:
    media = media
    conceito = 'A'
    print('Entre 9.0 e 10.0                   {}      Aprovado'.format(conceito))
elif 7.5 < media < 9.0:
    media = media
    conceito = 'B'
    print('Entre 7.5 e 9.0                    {}      Aprovado'.format(conceito))
elif 6.0 < media < 7.5:
    media = media
    conceito = 'C'
    print('Entre 6.0 e 7.5                    {}      Aprovado'.format(conceito))
elif 4.0 < media < 6.0:
    media = media
    conceito = 'D'
    print('Entre 4.0 e 6.0                    {}      Reprovado'.format(conceito))
elif 4.0 > media > 0:
    media = media
    conceito = 'E'
    print('Entre 4.0 e zero                   {}      Reprovado'.format(conceito))
else:
    print('Error')
print('=-'*20)


