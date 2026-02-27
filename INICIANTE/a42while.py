frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    quantas_vezes_letra_apareceu = frase.count(letra_atual)


    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual

    elif qtd_apareceu_mais_vezes == quantas_vezes_letra_apareceu:
        if letra_atual not in letra_apareceu_mais_vezes:
            letra_apareceu_mais_vezes = letra_apareceu_mais_vezes + "," + letra_atual

    i += 1

print(
    'A(s) letra(s) que apareceu(ram) mais vezes foi "'
    f'{letra_apareceu_mais_vezes}" que apareceu(ram) '
    f'{qtd_apareceu_mais_vezes}x vezes')
