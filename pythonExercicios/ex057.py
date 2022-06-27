sexo = str(input('Informe um sexo: [M/F]')).strip().upper()[0]  # Fatiamento [0] escolhe a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados Invalidos! Informe um sexo: [M/F]')).strip().upper()[0]
print('Sexo {} registrado!'.format(sexo))
