a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi: {} '.format(maior))
print('O menor valor digitado foi: {}'.format(menor))

#solução antiga
'''if a < b:
    if b > c:
        print('O maior é {}'.format(b))
        if c > a:
            print('O menor é {}'.format(a))
        else:
            print('O menor é {}'.format(c))
    else:
        print('O maior é {}'.format(c))
        print('O menor é {}'.format(a))
else:
    if a < c:
        print('O maior é {}'.format(c))
    else:
        print('O maior é {}'.format(a))
        if b > c:
            print(('O menor é {}'.format(c)))
        else:
            print('O menor é {}'.format(b))'''
