# num = (2, 5, 9, 1) # tupla
num = [2, 5, 9, 1]  # lista
num[2] = 3  # listas são mutaveis
num.append(7)  # Podemos adicionar valores na listas
num.sort()  # Podemos ordenar
num.sort(reverse=True)  # Podemos ordenar de trás pra frente
num.insert(2, 0)  # Podemos adicionar um valor em uma determinada posição, não elimina o valor que está na posição escolhida
num.pop()   # Elimina o ultimo valor
num.pop(2)  # Elimina o valor na posição determinada

# Elimina o valor escolhido, se existir valores iguais ele elimina apenas o primeiro valor encontrado,
num.remove(2)  # para eliminar todos os valores iguais é preciso usar um laço.

print('--'*30)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')  # Função "len" mostra uma contagem dos elementos

print('--'*30)
# ---------------------------------------------------------------
valores = list()  # Outra forma para definir uma lista

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))  # Podemos add valores pelo teclado

# valores.append(5)   # Add valores na lista
# valores.append(9)   # Add valores na lista
# valores.append(4)   # Add valores na lista

print('--'*30)

for v in valores:
    print(v)

print('--'*30)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

print('--'*30)
# ------------------------------------------------------
# a = [2, 3, 4, 7]
# b = a # Quando fazemos isso criamos uma ligação entre as listas, qualquer alteração afeta a outra
# b[2] = 8 # altera o valor na posição indicada e afeta todas as listas que foram criadas uma ligação

a = [2, 3, 4, 7]
b = a[:]  # Podemos usar [:] para fazer uma copia da lista, isso não cria uma ligação entre as listas
b[2] = 8    # Sem criar uma ligação, podemos alterar somente os valores da lista desejada

print(f'Lista A: {a}')
print(f'Lista B: {b}')
