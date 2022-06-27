produto = float(input('Qual é o preço do produto? R$'))
resultado = produto - (produto * 5 / 100)
print('O produto de custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto, resultado))


