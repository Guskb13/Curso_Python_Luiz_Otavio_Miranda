# ==============================
# DECORADORES COM PARÂMETROS
# ==============================

# Variável global usada apenas para mostrar
# quantas vezes a fábrica de decoradores foi chamada
contador = 0


def fabrica_de_decoradores(a=None, b=None, c=None):
    """
    Esta função NÃO é o decorador ainda.
    Ela é uma FÁBRICA de decoradores.

    Recebe parâmetros (a, b, c) e devolve um decorador
    configurado com esses valores.
    """
    global contador
    contador += 1  # Executa no momento da CRIAÇÃO do decorador

    def fabrica_de_funcoes(func):
        """
        Este é o DECORADOR de fato.
        Ele recebe a função que será decorada.
        """
        # Executa assim que a função é decorada
        print(f'Decoradora {contador}')

        def aninhada(*args, **kwargs):
            """
            Esta função SUBSTITUI a função original.
            Ela envolve a chamada da função decorada.
            """
            # Usa os parâmetros capturados pela closure (a, b, c)
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')

            # Chamada da função original
            res = func(*args, **kwargs)

            return res

        # Retorna a função wrapper
        # Wrapper é uma função que envolve outra função
        return aninhada

    # Retorna o decorador configurado
    return fabrica_de_funcoes


# ==============================
# USO DO DECORADOR COM @
# ==============================

# Isso é equivalente a:
# soma = fabrica_de_decoradores(1, 2, 3)(soma)
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


# ==============================
# USO MANUAL DO DECORADOR
# ==============================

# Cria um decorador sem parâmetros
decoradora = fabrica_de_decoradores()

# Aplica o decorador manualmente a uma função lambda
multiplica = decoradora(lambda x, y: x * y)


# ==============================
# CHAMADA DAS FUNÇÕES DECORADAS
# ==============================

# Aqui executa a função aninhada, NÃO a soma original diretamente
dez_mais_cinco = soma(10, 5)

# Aqui executa a função aninhada que envolve o lambda
dez_vezes_cinco = multiplica(10, 5)


# ==============================
# RESULTADOS FINAIS
# ==============================

print(dez_mais_cinco)     # 15
print(dez_vezes_cinco)   # 50