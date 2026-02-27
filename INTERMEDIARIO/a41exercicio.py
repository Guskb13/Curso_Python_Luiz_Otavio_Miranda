
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from dadosExercicio41.dados import produtos
import copy
import pprint

print(*produtos, sep='\n')
print()
print()
print()

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# Exercicio 1:

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [
    {**novos_produtos, 'preco': novos_produtos['preco'] * 1.1}
    for novos_produtos in novos_produtos
]
print(*novos_produtos, sep='\n')
print()
print()
print()

# Exercicio 2:

produtos_ordenados_por_nome = copy.deepcopy(produtos)

produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key = lambda item: item['nome'], reverse = True)
print(*produtos_ordenados_por_nome, sep='\n')
print()
print()
print()


# Exercicio 3:

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key = lambda item: item['preco'])
print(*produtos_ordenados_por_preco, sep='\n')
print()
print()
print()

# print(*produtos, sep='\n')


