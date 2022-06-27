print('=-'*24)
print('Álcool:\n'
      'até 20 litros, desconto de 3% por litro\n'
      'acima de 20 litros, desconto de 5% por litro\n'
      'Gasolina:\n'
      'até 20 litros, desconto de 4% por litro\n'
      'acima de 20 litros, desconto de 6% por litro')
print('-='*24)
litrosVendidos = int(input('Quantos litros foram vendidos? '))
combustivel = str(input('A - Alcool || G - Gasolina\n'
                        'Qual o tipo do combustivel? ')).upper()
if combustivel == 'A':
    if litrosVendidos <= 20:
        preco = 1.90 * litrosVendidos
        desconto = preco * 0.03
        valorFinal = preco - desconto
    elif litrosVendidos > 20:
        preco = 1.90 * litrosVendidos
        desconto = preco * 0.05
        valorFinal = preco - desconto
    print('Utilizando o combustivel Alcool, pagarar {:.2f}'.format(valorFinal))
elif combustivel == 'G':
    if litrosVendidos <= 20:
        preco = 2.50 * litrosVendidos
        desconto = preco * 0.04
        valorFinal = preco - desconto
    elif litrosVendidos > 20:
        preco = 2.50 * litrosVendidos
        desconto = preco * 0.06
        valorFinal = preco - desconto
    print('Utilizando o combustivel Gasolina, pagarar {:.2f}'.format(valorFinal))
    
