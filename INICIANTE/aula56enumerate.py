"""
enumerate - enumera iteraveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Gustavo')

#lista_enumerada = enumerate(lista)

'''for item in enumerate(lista):
    print(item)
    
    
print('\n\n')

for item in enumerate(lista, start = 2):
    print(item)
    
lista_enumerada2 = list(enumerate(lista))
'''

#for item in enumerate(lista):
 #   indice, valor = item
 #   print(item)
    
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
    
#for tupla_enumerada in enumerate(lista):
#    print('FOR da tupla')
#    for valor in tupla_enumerada:
#        print(f'\t{valor}')