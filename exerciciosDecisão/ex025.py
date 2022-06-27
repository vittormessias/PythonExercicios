print('=-'*20)
print('("Sim" digite: 1 ou "Não" digite: 0)')
print('-='*20)
pergunta1 = int(input('Telefonou para a vitima?'))
pergunta2 = int(input('Esteve no local do crime?'))
pergunta3 = int(input('Mora perto da vitima?'))
pergunta4 = int(input('Devia para a vitima?'))
pergunta5 = int(input('Já trabalhou com a vitima?'))
resposta = pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5
if 2 >= resposta > 1:
    print('Suspeita')
elif 4 >= resposta >= 3:
    print('Cúmplice')
elif resposta == 5:
    print('Assassino')
else:
    print('Inocente')

