# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

"""
Listas em Python
Tipo list - Mutavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveus - índices e fatiamento
Métodos úteis: 
      append, insert, pop, del, clear, extend, +
      Create Read Update  Delete = lista[i] (CRUD)
"""
import os

tarefas = []
lixo = []

while True:
    print('Comandos: listar, desfazer, refazer')
    x = input('Digite uma tarefa ou comando: ')
    print()
    
    
    if x == 'listar':
        if len(tarefas) == 0:
            print('Nenhuma tarefa para listar')
            continue
        print('TAREFAS:')
        for tarefa in tarefas:
            print(tarefa)
            
            
    elif x == 'desfazer':
        if len(tarefas) == 0:
            print('Nada a desfazer')
            continue
        lixo.append(tarefas[-1])
        tarefas.pop()
        print('TAREFAS:')
        for tarefa in tarefas:
            print(tarefa)
        print()
        
        
    elif x == 'refazer':
        if len(lixo) == 0:
            print('Nada a refazer')
            continue
        tarefas.append(lixo[-1])
        lixo.pop()
        print('TAREFAS:')
        for tarefa in tarefas:
            print(tarefa)
        print()
    elif x == 'clear':
        os.system('cls')
        continue
        
    else:
        tarefas.append(x)
        print('TAREFAS:')
        for tarefa in tarefas:
            print(tarefa)
        print()