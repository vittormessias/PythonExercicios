# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
b = ('onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
c = a + b
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
while True:
    usuario = int(input('Digite um numero entre 0 e 20: '))
    if 20 >= usuario >= 0:
        print(f'Você digitou o numero {c[usuario]}')
        user = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if user == 'N':
            break
print('FIM DO PROGRAMA')

