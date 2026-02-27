primeiro_valor = input('Digite um valor ')
segundo_valor = input('Digite outro valor ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} eh maior que o {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor} eh maior que o {primeiro_valor}')
else:
    print('Os valores sao iguais')