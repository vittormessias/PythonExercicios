'''Estrutura Condicional Aninhada'''
nome = str(input('Qual é o seu nome? '))
if nome == 'Vitor':
    print('\033[7;36mQue nome bonito\033[m')
elif nome == 'Pedro' or nome == 'Paulo' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Julina Jessica Claudia ':
    print('Belo nome Feminino')
'''else:'''
'''print('Seu nome é bem normal.')'''
print('Tenha um bom dia, {}!'.format(nome))
