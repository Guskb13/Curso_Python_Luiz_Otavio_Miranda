

# EU QUE FALEI DE ARGS E KWARGS, CODIGO DA AULA ABAIXO
"""
*args e **kwargs em Python permitem funções flexíveis que aceitam um número
variável de argumentos: *args coleta argumentos posicionais (sem nome) em
uma tupla, enquanto **kwargs coleta argumentos nomeados (chave=valor)em um
dicionário, sendo que *args vem antes de **kwargs na definição da função.
A diferença principal é que *args lida com quantidades de argumentos sem nome,
e **kwargs lida com nomes (chaves) e valores. 

def soma(*args):
    total = 0
    for valor in args:
        total += valor
    return total

soma(1, 2, 3, 4)


def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_dados(nome="Gustavo", idade=22, curso="Computação")

"""


# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

# Funções decoradoras são úteis para adicionar comportamentos transversais 
# a funções ou métodos, de forma reutilizável, organizada e sem modificar
# o código original. Elas resolvem problemas clássicos de engenharia de 
# software relacionados a separação de responsabilidades.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
