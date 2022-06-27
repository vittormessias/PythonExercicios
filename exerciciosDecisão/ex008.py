produto1 = float(input('Digite o preço em R$ de um produto: '))
produto2 = float(input('Digite o preço em R$ de um outro produto: '))
produto3 = float(input('Digite o preço em R$ de mais um produto: '))
maisBararto = produto1
if produto2 < produto1 and produto2 < produto3:
    maisBararto = produto2
if produto3 < produto1 and produto3 < produto2:
    maisBararto = produto3
print('Levar o produto no valor de R${:.2f}'.format(maisBararto))


"""prod_1 = float(input('Valor 1° produto: '))
prod_2 = float(input('Valor 2° produto: '))
prod_3 = float(input('Valor 3° produto: '))

if prod_1 <= prod_2 and prod_1 <= prod_3:
    print('Compre o primeiro produto.')
elif prod_2 <= prod_3:
    print('Compre o segundo produto.')
else:
    print('Compre o terceiro produto')"""