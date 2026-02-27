"""
Iterando strings com while
"""
nome = 'Gustavo Cabral Goncalves'
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[4])

contador = 0
novo_nome = ''

while contador < tamanho_nome:
    letra = nome[contador]
    #novo_nome += letra
    #novo_nome += '*'
    novo_nome += f'*{letra}'
    contador += 1

print(novo_nome)