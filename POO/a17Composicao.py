# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.


# COMPOSIÇÃO: UM OBJETO GERENCIA O CICLO DE VIDA DE OUTRO OBJETO
# Um objeto é dono e cria outro objeto

"""
Cliente cria e é dono do Endereço
O endereço nasce dentro do cliente
Se o cliente é apagado, os endereços também são
O ciclo de vida está fortemente ligado


Observação importante (nível prova 👀):
O método inserir_endereco_externo quebra a composição,
pois aceita um endereço criado fora — isso vira agregação
nesse ponto específico.
"""


"""
Associação: "Vitor usa a caneta". (Relação de igualdade/ajuda).
Agregação: "O Carrinho tem produtos". (Relação de contêiner/conteúdo).
Composição: "O Humano é dono do coração". (Relação de existência/vida).
"""

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1


print(endereco_externo.rua, endereco_externo.numero)
print('######################## AQUI TERMINA MEU CÓDIGO')