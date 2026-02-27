# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json


import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, 'a8.json')

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
p1 = Pessoa('Gustavo', 21)
p2 = Pessoa('Duda', 20)
p3 = Pessoa('Vitor', 27)

bd = [vars(p1), vars(p2), vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()