# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados
s2 = set('Gustavo')
# print(s1)
# print(s2)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s3 = set()
s3 = {1, 2, 3, 3, 3, 3, 3, 1}
# print(s3)

l1 = [1, 1, 1, 1, 2, 2, 3, 3, 1]
s4 = set(l1)
#print(s4)
l2 = list(s4)
#print(l2)

# print(2 in s4)

# for numero in s4:
#     print(numero)


# Métodos úteis:
# add, update, clear, discard
s5 = set()
s5.add('Luiz')
s5.add(1)
s5.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s5.discard('Olá mundo')
# print(s1)



# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s6 = {1, 2, 3}
s7 = {2, 3, 4}
s8 = s6 | s7
s9 = s6 & s7
s10 = s6 - s7
s11 = s7 - s6
s12 = s6 ^ s7
# s8 = s6.union(s7)
print(s8)
print(s9)
print(s10)
print(s11)
print(s12)