# Altere o programa anterior (4) permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.
anos = 0
while True:
    habitantesA = int(input('Digite a população: '))
    taxaA = float(input('Digite uma taxa de crescimento: '))
    habitantesB = int(input('Digite uma outra população: '))
    taxaB = float(input('Digite uma taxa de crescimento: '))
    while habitantesA <= habitantesB:
        habitantesA = habitantesA + (habitantesA * taxaA)
        habitantesB = habitantesB + (habitantesB * taxaB)
        anos += 1
    usuario = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if usuario == 'N':
        break
print(f'Foram necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B')
