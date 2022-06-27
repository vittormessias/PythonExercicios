# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido
for c in range(0, 10):
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if 10 >= nota > 0:
        print('Valor Válido')
        break
    else:
        print('Valor inválido')

