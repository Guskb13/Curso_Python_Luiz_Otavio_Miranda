# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total
    
numeros = 1, 43, 1, 2, 2
print(type(numeros))

resultado = multiplica(*numeros)

print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def ParouImpar(a):
    if a % 2 == 0:
        return print(f'O numero', a, 'é par')
    return print(f'O numero', a, 'é impar')
    
resultado = ParouImpar(4)
