lista = list()
while True:
    nome = (str(input('Nome: ')))
    nota1 = float(input('Primeira Nota: '))
    nota2 = float(input('Segunda Nota: '))
    media = (nota1 + nota2) / 2

    lista.append([nome, [nota1, nota2], media])

    usuario = str(input('Deseja continuar? [S/N]'))[0]
    if usuario in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}  {"Nome":<10}  {"Média":>8}')
print('-' * 26)

for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')

print('-' * 20)

while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if escolha == 999:
        break
    if escolha <= len(lista) - 1:
        print(f'Notas de {lista[escolha][0]} são {lista[escolha][1]}')
print('FIM')
