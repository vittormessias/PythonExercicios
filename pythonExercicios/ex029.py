velocidade = float(input('Digite uma velocidade KM/H: '))
if velocidade > 80:
    velocidade = 7 * (velocidade - 80)
    print('Você foi multado! {:.2f}'.format(velocidade))
else:
    print('Você está abaixo do limite! Boa Viagem!')