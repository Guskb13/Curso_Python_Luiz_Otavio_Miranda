"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


'''

num_str = (input('Digite um numero inteiro: '))

try:
    num_int = int(num_str)
    print('É um número inteiro mesmo')

    if num_int % 2 == 0:
        print('Você digitou um número par!')
    else:
        print('Você digitou um número ímpar!')
except ValueError:
    print('Você não digitou um número inteiro!')

'''

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


horario_str = (input('Digite somente que horas sao onde voce esta!!: '))

try:
    horario_num = int(horario_str)

    if horario_num <=11 and horario_num >= 0:
        print('Bom dia flores do dia')
    elif horario_num <=17 and horario_num >= 12:
        print('Boa tarrrrde')
    elif 18 <= horario_num <= 23:
        print('Boa, a noite é uma criança!')
    else:
        print('Digite um horário válido (entre 0 e 23).')

except ValueError:
    print('Por favor, digite somente o numero das horas!')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

'''
nome = (input('Digite seu nome: '))


tamanho_do_nome = len(nome)

if tamanho_do_nome <= 4:
    print('Seu nome é curto')
elif tamanho_do_nome > 4 and tamanho_do_nome < 7:
     print('Seu nome é normal')
else:
     print('Seu nome é muito grande')

'''

