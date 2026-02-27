# Variáveis livres + nonlocal (locals, globals)

# Variavues locais são definidas dentro de uma função e
# existem apenas durante a execução dessa funçao
"""
def f():
    x = 10  # variável local
    print(x)

f()
# print(x)  -> erro: x não existe fora da função

"""

# Varáveis Globais são definidas fora de qualquer função,
# no escopo do módulo (arquivo)
"""
x = 5  # variável global

def f():
    print(x)

f()

#########

x = 5

def f():
    global x
    x = 10

f()
print(x)  # 10
"""


# Variáveis nonlocal pertencem ao escopo de uma função externa,
# mas não são globais
"""
def externa():
    x = 10

    def interna():
        nonlocal x
        x = 20

    interna()
    print(x)

externa()  # 20
"""

# Variáveis livres é usada dentro de uma função, 
# não é definida localmente nessa função e nem passada como parâmetro
# vinda do escopo externo
"""
def externa():
    x = 10

    def interna():
        print(x)  # x é uma variável livre

    interna()
"""


# CODIGO DO PROFESSOR

# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())



def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)