nota1 = float(input('\033[32mDigite uma nota: \033[m '))
nota2 = float(input('\033[36mDigite uma outra nota: \033[m'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Reprovado! Media {}'.format(media))
elif 6.9 > media >= 5.0:
    print('Recuperação! Media {}'.format(media))
elif media >= 7.0:
    print('Aprovado! Media {}'.format(media))
