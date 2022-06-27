km = float(input('Digite uma distancia em KM:'))
if km <= 200:
    final = km * 0.50
    print('Total a pagar {:.2f}'.format(final))
else:
    final = km * 0.45
    print('Total a pagar {:.2f}'.format(final))

