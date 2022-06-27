while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break  # Para parar quando for negativo
    for cont in range(1, 11):
        print(f'{tabuada} x {cont} = {tabuada * cont}')
print('Programa tabuada encerrada! Volte sempre!')


