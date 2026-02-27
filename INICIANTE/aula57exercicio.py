"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indices inexistentes
"""

# MEU CODIGO
import os

Lista_compras = []

contador = -1

while True:
    acao = input('Selecione uma opção:\n[i]nserir  [a]pagar  [l]istar\n')
    
    if acao == 'i':
        os.system('cls')
        Lista_compras.append(input('Digite o item\n'))
        contador+= 1
        
    elif acao == 'a':
        try:
            indice = int(input('Qual indice deseja apagar?\n'))
        except ValueError:
            print('Digite apenas numeros inteiros')
        if indice > contador:
            print('Não foi possível apagar este indice')
            continue
        print(Lista_compras[indice], 'do indice', indice, 'Apagado')
        del Lista_compras[indice] 
        
    elif acao =='l':
        os.system('cls')
        
        if contador < 0:
            print('A lista não possui elementos')
            
        for indice, Item in enumerate(Lista_compras):
            print(indice, Item)
    else:
        print('Por favor escolha i, a ou l')
            
        
#CODIGO DO PROFESSOR        
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
"""