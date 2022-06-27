matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


'''matriz = list()
v1 = list()
v2 = list()
v3 = list()
for c in range(0, 3):
    v1.append(int(input(f'Digite um valor para {[0, c]}: ')))

for c in range(0, 3):
    v2.append(int(input(f'Digite um valor para {[1, c]}: ')))

for c in range(0, 3):
    v3.append(int(input(f'Digite um valor para {[2, c]}: ')))
print('-='*30)

matriz.append(v1[:])
v1.clear()
matriz.append(v2[:])
v2.clear()
matriz.append(v3[:])
v3.clear()

print([matriz[0][0]], end=' ')
print([matriz[0][1]], end=' ')
print([matriz[0][2]])

print([matriz[1][0]], end=' ')
print([matriz[1][1]], end=' ')
print([matriz[1][2]])

print([matriz[2][0]], end=' ')
print([matriz[2][1]], end=' ')
print([matriz[2][2]])'''
