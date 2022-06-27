# Tuplas são estruturas compostas
# Tuplas são imutáveis, não dá para mudar seus valores # lanche[1] = 'Sorvete'  # Essa linha não funciona
# Tuplas aceitam dados de tipos diferentes(String, int) dentro delas
pessoa = ('Vitor', 20, 'M', 80)
# del(pessoa) # comando "del" exclui uma tupla, não dá para excluir um item, somente a tupla inteira
print(pessoa)

print('=-'*10)
a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = b + a  # Junta as tuplas e forma uma tupla só. Não soma!
print(c)
print(len(c))  # len(retornar o número de itens que tem dentro)
print(c.count(5))  # count mostra quantas vezes tal coisa aparece
print(c)
print(c.index(8))  # index mostra em qual posição tal coisa está
print(c.index(5, 1))  # index com deslocamento, mostra a posição de tal coisa

print('=-'*10)
lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')  # Pode ser sem parenteses
# print(lanche[-3:]) posições
print(sorted(lanche))  # Mostra de forma ordenada
print('=-'*10)
# for com contador, com len(retornar o número de itens que tem dentro)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na pisição {cont}')
print('Comi pra caramba!')

print('=-'*10)
# for sem contador(não dar a posição)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('=-'*10)
# For com contador(dar uma posição) com enumerate (retorna uma tupla com um número sequencial e um item da sequência correspondente)
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na pisição {posicao}')
print('Comi pra caramba!')
