nome = str(input('Digite um nome: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(nome.upper().count('A')))
print('A letra A aparece na posiçaõ {}'.format(nome.upper().find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(nome.upper().rfind('A')+1))
