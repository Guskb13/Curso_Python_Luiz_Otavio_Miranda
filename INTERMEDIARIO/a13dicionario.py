# Manipulando chaves e valores em dicionarios

pessoa = {}


chave = 'nome'

pessoa[chave] = 'Gustavo'
pessoa['sobrenome'] = 'Messi'

print(pessoa[chave])

pessoa[chave] = 'Lionel'

print(pessoa)

del pessoa['sobrenome']
print(pessoa)
print(pessoa[chave])


print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
    

