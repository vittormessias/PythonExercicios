n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma outra nota: '))
n3 = float(input('Digite mais uma nota: '))
media = (n1 + n2 + n3) / 3
if media >= 7:
    print('Aprovado, sua media foi {:.1f}'.format(media))
elif media < 7:
    print('Reprovado, sua media foi {:.1f}'.format(media))
elif media == 10:
    print('Aprovado com Distinção')
