nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite outra nota: '))
media = (nota1 + nota2) / 2
if media == 10:
    print('Aprovado com Distinção! {}'.format(media))
else:
    if media >= 7:
        print('Aprovado! Sua media foi: {}'.format(media))
    else:
        print('Reprovado! Sua media foi: {}'.format(media))


