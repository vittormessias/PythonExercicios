# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
mediaIdade = 0
somaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
cont = 0
for p in range(1, 5):
    print('----- {}° Pessoa -------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    genero = str(input('Gênero: [M/F]')).strip()
    # No final do programa, mostre: a média de idade do grupo
    somaIdade += idade
    if p == 1 and genero in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    # qual é o nome do homem mais velho
    if idade > maiorIdadeHomem and genero in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    # e quantas mulheres têm menos de 20 anos.
    if idade < 20 and genero in 'Ff':
        cont += 1
mediaIdade = somaIdade / 4
print('A media de idade é: {}'.format(mediaIdade))
print('O nome do homem mais velho é {} e tem {} anos'.format(nomeVelho, maiorIdadeHomem))
print('Há {} mulheres com menos de 20 anos'.format(cont))
