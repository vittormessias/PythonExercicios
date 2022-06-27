print('\033[7;30;44mOlá, Munddo!\033[m')
a = 3
b = 5
print('Os valores são \033[4;34;40m{}\033[m e \033[7;30;42m{}\033[m!!!'.format(a, b))
nome = 'vitruviano'
cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoeBranco':'\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
