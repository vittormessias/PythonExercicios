lado1 = int(input('Digite um lado de um triângulo: '))
lado2 = int(input('Digite um outro lado de um triângulo: '))
lado3 = int(input('Digite mais um lado de um triângulo: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Da para formar um triângulo!')
    if lado1 == lado2 == lado3:
        print('Equilátero')
    if lado1 == lado2 and lado2 != lado3 or lado3 == lado1 and lado2 != lado3:
        print('Isósceles')
    if lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print('Escaleno')
else:
    print('Não dá para formar um triângulo!')
