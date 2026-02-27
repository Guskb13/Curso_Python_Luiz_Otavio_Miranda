# Generator expression, Iterables e Iterators em Python
# Generator expression = Funções que sabem pausar em determinada ocasiao

# Generator é bom pois gasta menos espaço no sistema, é mais modular 
# mais fácil de ler o código, porém não armazena os dados anteriores
# para isso coloque o gerador dentro de uma lista

# list(gen_primes(50,100))



import sys

iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__()
iterator = iter(iterable)

lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
# print(lista)

for n in generator:
    print(n)



