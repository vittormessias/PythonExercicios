# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
tabuada = int(input('Quer ver a tabuada de qual numero entre 1 e 10? '))
while True:
    if not 10 >= tabuada > 1:
        print('Entre 1 e 10..')
        tabuada = int(input('Quer ver a tabuada de qual numero? '))
    else:
        for c in range(1, 11):
            multi = tabuada * c
            print(f'{tabuada} * {c} = {multi}')
        break
