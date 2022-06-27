print('{:=^40}'.format(' LOJAS VITRUVIANO '))
produto = float(input('Digite o valor do produto: R$ '))
formaPagamento = int(input('Qual vai ser a forma de pagamento? \n' '1 - \033[4mÀ vista\033[m\n' 
                           '2 - \033[4mÀ vista no cartão\033[m\n' '3 - \033[4mEm até 2x no cartão\033[m\n' 
                           '4 - \033[4m3x ou mais no cartão\033[m\n'': '))
if formaPagamento == 1:
    desconto = produto - (produto * 10 / 100)
    print('Valor à pagar: {:.2f}'.format(desconto))
elif formaPagamento == 2:
    desconto = produto - (produto * 5 / 100)
    print('Valor à pagar: {:.2f}'.format(desconto))
elif formaPagamento == 3:
    desconto = produto
    parcela = produto / 2
    print('Parcelada em 2x sem juros de {:.2f} do valor total de {}'.format(parcela, desconto))
elif formaPagamento == 4:
    desconto = produto + (produto * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parcela = desconto / parcelas
    print('Parcelada em {}x de {:.2f} COM JUROS. Do valor total de R${:.2f}'.format(parcelas, parcela, desconto))
else:
    total = 0
    print('Opção Invalida')
print('-='*30)
