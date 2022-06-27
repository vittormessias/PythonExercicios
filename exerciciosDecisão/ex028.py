print('=-'*30)
print('                    Até 5 Kg    Acima de 5 Kg\n'
      'File Duplo    R$ 4.90 por Kg   R$ 5.80 por Kg\n'
      'Alcatra       R$ 5.90 por Kg   R$ 6.80 por Kg\n'
      'Picanha       R$ 6.90 por Kg   R$ 7.80 por Kg')
print('-='*30)
tipoCarne = str(input('Qual o tipo de carne? ')).lower()
quantidadeCarne = int(input('Qual a quantidade de carne? '))
cartao = str(input('A compra vai ser feita no cartão Tabajara? (Sim ou Não) ')).lower()
if cartao == 'sim':
    if quantidadeCarne > 5 and tipoCarne == 'file duplo':
        preco = quantidadeCarne * 5.80
        desconto = preco * 0.05
        valorFinal = preco - desconto
    elif quantidadeCarne > 5 and tipoCarne == 'alcatra':
        preco = quantidadeCarne * 6.80
        desconto = preco * 0.05
        valorFinal = preco - desconto
    elif quantidadeCarne > 5 and tipoCarne == 'picanha':
        preco = quantidadeCarne * 7.80
        desconto = preco * 0.05
        valorFinal = preco - desconto
    print('=-'*30)
    print('Quantidade de Carne: {}\n'
          'Preço total: {}\n'
          'Tipo de Pagamento: Cartão Tabajara\n'
          'Valor do desconto: 5%\n'
          'Valor a Pagar: {}'.format(quantidadeCarne, preco, valorFinal))
    print('-='*30)
else:
    if quantidadeCarne > 5 and tipoCarne == 'file duplo':
        preco = quantidadeCarne * 5.80
    elif quantidadeCarne > 5 and tipoCarne == 'alcatra':
        preco = quantidadeCarne * 6.80
    elif quantidadeCarne > 5 and tipoCarne == 'picanha':
        preco = quantidadeCarne * 7.80
    print('=-'*30)
    print('Quantidade de Carne: {}\n'
          'Preço total: {}\n'
          'Tipo de Pagamento: Dinheiro\n'
          'Valor do desconto: 0\n'
          'Valor a Pagar: {}'.format(quantidadeCarne, preco, preco))
    print('-='*30)
