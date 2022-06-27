# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
nome = str(input('Digite um nome: ')).strip().upper().split()
list = [0, 4]
for c in enumerate(nome, 4):
    if c == nome:
        print(nome)
        list.append(c)
    else:
        print(list)