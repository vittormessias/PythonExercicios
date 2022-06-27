s = 0
for c in range(0, 4):
    n = int(input('Digite um numero: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))

#exemplo2
for c in range(0, 10):
    n = int(input('Digite um valor: '))
print('FIM!')

#exemplo3
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')