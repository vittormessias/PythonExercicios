total = cont = contProduto = menor = 0
produto = ' '
while True:
    nome = str(input('Produto: '))
    preco = float(input('Preço: '))
    total += preco
    cont += 1
    if preco > 1000:
        contProduto += 1
    if cont == 1 or preco < menor:
        menor = preco
        produto = nome
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'Total gastos na compra: \033[32m{total:.2f}\033[m')
print(f'Total de produtos custam mais de R$1000: \033[34m{contProduto}\033[m.')
print(f'Nome do produto mais barato foi o \033[33m{produto}\033[m que custa {menor:.2f}')
