"""Cuidado com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""

nome = 'Luiz'
noutra_variavel = nome
nome = 'João'

print(nome)
print(noutra_variavel)


lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()

# para a lista_b nao apontar para o mesmo enderelo de 
# memoria que a lista_a, use lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'

# lista_a e lista_b apontam para o mesmo valor da memoria

# quando o valor for imutavel eu estou copiando o valor para
# outro quando uso o sinal de igual, quando o valor for 
# mutavel eu aponto para o mesmo endereço de memoria


print(lista_a)
print(lista_b)

