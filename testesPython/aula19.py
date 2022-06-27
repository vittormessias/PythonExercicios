# Dicionarios
pessoas = {'nome': 'Vitor', 'sexo': 'M', 'idade': '20'}  # Declarar com keys {}
print(pessoas)
print('='*20)
print(pessoas['nome'])
print('='*20)
print(pessoas['idade'])
print('='*20)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')  # Aspas duplas dentro de aspas simples com format
print('='*20)
print(pessoas.keys())  # mostra o nome do indice
print('='*20)
print(pessoas.values())  # mostra os valores
print('='*20)
print(pessoas.items())  # mostra os itens que estão dentro do dicionário
print('='*20)
for k in pessoas.keys():  # mostra o nome do indice
    print(k)
print('='*20)
for k in pessoas.values():  # mostra os valores
    print(k)
print('='*20)
for k in pessoas.items():  # mostra os itens que estão dentro do dicionário
    print(k)
print('='*20)
del pessoas['sexo']  # Comando para apagar um indice
for k, v in pessoas.items():  # com dicionários usamos itens ao inves do comando enumerate
    print(f'{k} = {v}')
print('='*20)
pessoas['nome'] = 'Messias'  # Comando para substituir um valor
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('='*20)
pessoas['peso'] = 80  # Comando para adicionar um indice com um valor
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('='*26)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}  # Declaramos o nome do indice e os valores dentro do dicionario
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)  # Add um dicionario dentro de uma lista
brasil.append(estado2)

print(brasil[0])  # Seleciona a lista e o indice
print(brasil[1]['sigla'])  # Seleciona a lista e o indice e dentro escolhemos o indice do dicionario para exibir

print('='*26)
estado = dict()  # Declaração de um dicionario
brasil = list()  # Declaração de uma lista
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla Federativa: '))
    brasil.append(estado.copy())  # Com dicionários, para fazer uma "copia/fatiamento" usamos o comando copy() e não [:]
print(brasil)
print('='*20)
for e in brasil:
    print(e)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print('='*20)
for e in brasil:  # Lista
    for k, v in e.items():  # Dicionario
        print(f'O campo {k} tem valor {v}.')
print('='*20)
for e in brasil:  # Lista
    for v in e.items():  # Dicionario
        print(v, end=' ')
    print()
