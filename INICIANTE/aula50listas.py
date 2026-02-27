"""
Listas em Python
Tipo list - Mutavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveus - índices e fatiamento
Métodos úteis: 
      append, insert, pop, del, clear, extend, +
      Create Read Update  Delete = lista[i] (CRUD)
"""
# é bom de usar del no final de uma lista, pois ao usar del 
# começo da lista, é necessário mover todos os outros itens
# uma casa a esquerda e isso gasta memória O(n)

#    append adiciona um item no fim da lista
#    pop remove o ultimo elemento da lista
#    insert adiciona um intem no indice escolhido
#    clear limpa a lista
#    extend estende a lista
#    + concatena listas

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)
print(lista_a)

