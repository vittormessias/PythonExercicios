aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')


'''lista = []   

nome = {'nome': str(input("Nome: "))}
media = {'media': float(input(f'Media de {nome["nome"]}: '))}

lista.append(nome.copy())
lista.append(media.copy())

print(f'Nome é igual a {lista[0]["nome"]}')

print(f'Média é igual a {lista[1]["media"]}')

if 7 <= lista[1]["media"]:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')'''

