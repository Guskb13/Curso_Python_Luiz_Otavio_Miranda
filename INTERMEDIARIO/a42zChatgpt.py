def subtrai(x, y):
    return x - y


def divide(x, y):
    return x / y


def criar_funcao(funcao, x, modo):
    def interna(y):
        if modo == 'Esquerda':
            return funcao(x, y)
        else:
            return funcao(y, x)
    return interna


subtrai_de_10 = criar_funcao(subtrai, 10, 'Esquerda')
divide_por_2 = criar_funcao(divide, 2, 'Direita')

print(subtrai_de_10(4))
print(divide_por_2(4))
