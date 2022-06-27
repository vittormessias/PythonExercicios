largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura * altura
print('Sua parede tem a dimensão de {} X {} e sua área é de {}m²'.format(largura, altura, area))
tinta = area / 2
print('Para pintar sua parede, você precisará de {}l de tinta'.format(tinta))

