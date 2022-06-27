nome = str(input('qual é o seu nome? '))
if nome == 'Vitor':
    print('Que nome lindo você tem!')
else:
    print('Que nome normal que você tem!')
print('Bom dia! {}!'.format(nome))
'----------------------------------------'
n1 = float(input('Digite uma nota:'))
n2 = float(input('Digite uma outra nota: '))
m = (n1+n2)/2
print('A sua media foi {:.1f}'.format(m))
if m<=6:
    print('Media ruim')
else:
    print('Media boa!')