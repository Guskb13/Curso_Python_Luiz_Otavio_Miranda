"""
Listas em Python
Tipo list - Mutavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveus - índices e fatiamento
Métodos úteis: 
      append, insert, pop, del, clear, extend, +
      Create Read Update  Delete = lista[i] (CRUD)
"""
# é bom de usar del no final de uma lista, pois ao usar del no
# começo da lista, é necessário mover todos os outros itens
# uma casa a esquerda e isso gasta memória O(n)

# append adiciona um item no fim da lista
# pop remove o ultimo elemento da lista
# insert adiciona um intem no indice escolhido
# clear limpa a lista
# extend estende a lista
# + concatena listas


lista = [10, 20, 30, 40]
lista.append('Gustavo')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(0,5)
print(lista)

