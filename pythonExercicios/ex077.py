#  Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

#  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
for vogais in tupla:
    print(f'\nNa palvra {vogais} temos', end=' ')
    for letra in vogais:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
