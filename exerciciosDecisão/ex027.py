print('=-'*30)
print('                   Até 5 Kg    Acima de 5 Kg\n'
      'Morango      R$ 2.50 por Kg   R$ 2.20 por Kg\n'
      'Maçã         R$ 1.80 por Kg   R$ 1.50 por Kg')
print('-='*30)
morango = int(input('Quantos morangos foram adquiridos em Kg? '))
maca = int(input('Quantas maçãs foram adquiridas Kg? '))
if morango and maca > 8 or morango and maca > 25.00:
    preco = (morango * 2.20) + (maca * 1.50)
    desconto = preco * 0.10
    valorFinal = preco - desconto
    print('Valor a ser pago: {}'.format(valorFinal))
elif morango and maca <= 5 or morango and maca < 25.00:
    valorFinal = (morango * 2.50) + (maca * 1.80)
    print('Valor a ser pago: {}'.format(valorFinal))
