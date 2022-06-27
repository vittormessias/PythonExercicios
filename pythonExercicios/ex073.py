a = ('Corinthians', 'Santos', 'Avaí', 'América-MG', 'Bragantino', 'Atlético Mineiro', 'São Paulo', 'Botafogo',
     'Internacional', 'Coritiba')
b = ('Cuiaba', 'Atlhetico-PR', 'Palmeiras', 'Flamengo', 'Fluminense', 'Goiás', 'Ceará-SC', 'Juventude', 'Atlético-GO',
     'Fortaleza')
c = a + b
print(c[:5])  # 5 primeiros da tabela
print(c[-4:])  # 4 Ultimos da tabela
print(sorted(c))  # Ordem alfabética
print(c.index('Atlético Mineiro')+1)  # Mostra a posição
