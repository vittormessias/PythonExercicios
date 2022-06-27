# Soma dos pares
soma = 0  # Atribuição
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        soma += n
    else:
        print('Não há numeros pares')
print(soma)

