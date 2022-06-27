# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
for c in range(0, 10):
    usuario = str(input('Digite um nome de Usuário: ')).strip().upper()
    senha = str(input('Digite uma senha: ')).strip().upper()
    if usuario == senha:
        print('Error!')
    else:
        print('Sucesso!')
        break
