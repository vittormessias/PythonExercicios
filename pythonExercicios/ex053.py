# Detector de Palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()  # Função 'Strip' elimina espaços
palavras = frase.split()  # Função 'split' para separar as palavras
juntar = ''.join(palavras)  # Função 'Join' para juntar as palavras
inverso = ''
for letra in range(len(juntar) - 1, -1, -1):  # Função 'Len' lê a ultima letra
    inverso += juntar[letra]
print('O inverso de {} é {}'.format(juntar, inverso))
if inverso == juntar:
    print('PALINDROMO!')
else:
    print('Não é um PALINDROMO!')

