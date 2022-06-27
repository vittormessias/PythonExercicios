a = float(input('\033[32mDigite um numero:\033[m'))
b = float(input('\033[36mDigite um outro numero:\033[m'))
c = float(input('\033[34mDigite um outro numero:\033[m'))
'''Condição Aninhada'''
if a < b + c and b < a + c and c < a + b:
    print('Pode formar um triangulo ', end='')
    '''Ninho dentro do Ninho'''
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Não pode formar um triangulo')


'''Meu código antigo'''
'''if a < b + c and b < a + c and c < a + b:
    print('Pode formar um triangulo ', end='')
    ''''Duas formas de fazer um igual''''
    if a == b and b == c or a == b == c:
        print('Equilátero')
    elif a == b and a != c or b == c and b != a or c == a and c != b:
        print('Isóceles')
    elif a != b and a != c and b != a and b != c and c != a and c != b:
        print('Escaleno')
else:
    print('Não pode formar um triangulo')
'''