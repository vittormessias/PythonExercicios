cont = s = 0
while True:
    n = int(input('[999 para parar]\n'
                  'Digite um numero: '))
    if n == 999:
        break  # Para não somar e não contar o flag
    s += n
    cont += 1
print(f'A soma dos {cont} valores foi {s}')
