primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))
if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
    if segundo < terceiro:
        menor = segundo
        print(primeiro, terceiro, segundo)
    else:
        menor = terceiro
        print(primeiro, segundo, terceiro)
if segundo > primeiro and segundo > terceiro:
    maior = segundo
    if primeiro < terceiro:
        menor = primeiro
        print(segundo, terceiro, primeiro)
    else:
        menor = terceiro
        print(segundo, primeiro, terceiro)
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
    if primeiro < segundo:
        menor = primeiro
        print(terceiro, segundo, primeiro)
    else:
        menor = segundo
        print(terceiro, primeiro, segundo)
