peso = int(input('\033[32mDigite seu peso: (Kg)\033[m '))
altura = float(input('\033[36mDigite sua altura: (m)\033[m '))
final = peso / (altura ** 2)
if final < 18.5:
    print('Abaixo do peso! \n '
          '{:.1f}'.format(final))
elif 18.5 <= final < 25:
    print('Peso Ideal! \n'
          '{:.1f}'.format(final))
elif 25 <= final < 30:
    print('Sobrepeso \n'
          '{:.1f}'.format(final))
elif 30 <= final < 40:
    print('Obesidade \n'
          '{:.1f}'.format(final))
else:
    print('Obsidade mórbida \n'
          '{:.1f}'.format(final))
