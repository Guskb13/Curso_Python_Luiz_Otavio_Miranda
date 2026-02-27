"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Pyhton retornarm None (nada)
"""


# def Python(a, b, c):
#     print("Várias")
#     print("Várias")
#     print("Várias")
#     print("Várias")

# Python()

# def imprimir(a, b ,c):
#     print(a,b,c)

# imprimir(1,2,3)
# imprimir(4,5,6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')
    
saudacao("Gustavo")
saudacao()


