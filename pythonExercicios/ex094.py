galera = list()
pessoa = dict()
soma = media = 0
# Entradad de dados
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
# Saida de dados
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<< ENCERRADO >>')

# Solução Antiga
'''pessoas = dict()
lista = []
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    if pessoas['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        pessoas['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    usuario = str(input('Deseja continuar? [S/N]')).strip()[0]
    if usuario in 'Nn':
        break
    if usuario not in 'Ss':
        print('ERRO! Por favor, digite apenas S ou N')
        usuario = str(input('Deseja continuar? [S/N]')).strip()[0]
somaIdade = 0
for v in lista:
    somaIdade += v['idade']
mediaIdade = somaIdade / len(lista)
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A media de idade é de {mediaIdade:5.2f} anos.')
print(f'C) As mulheres cadastradas foram', end='')
for v in lista:
    if v['sexo'] == 'F':
        print(f'{v["nome"]} ', end='')
print()
print('D) lista das pessoas que estão acima da média: ')
for i in lista:
    if i['idade'] >= mediaIdade:
        print(f'    nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]};')
print('<< ENCERRADO >>')'''

