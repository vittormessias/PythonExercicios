a = float(input('Digite um numero: '))
b = float(input('Digite um numero: '))
c = float(input('Digite um numero: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')


#solução antiga
'''if A < B:
    if B > C:
        triangulo = A + C
        if triangulo > B:
            print('Da para formar um triangulo!')
        else:
            print('Não da para formar um triangulo!')
    else:
        triangulo = B + A
        if triangulo > C:
            print('Da para formar um triangulo!')
        else:
            print('Não da para formar um triangulo!')
else:
    if A > C:
        triangulo = B + C
        if triangulo > A:
            print('Da para fazer um triangulo!')
        else:
            print('Não da para fazer um triangulo!')
    else:
        triangulo = B + A
        if triangulo > C:
            print('Da para fazer um triangulo!')
        else:
            print('Não da para fazer um triangulo!')'''