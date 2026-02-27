# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# Uma instância é um objeto criado a partir da classe.
# É a “coisa de verdade” feita com o molde.

# Classe = planta da casa
# Instância = casa construída

# Um método é uma função que pertence à classe e que 
# define um comportamento dos objetos.
# Para usar um método, você chama ele a partir da instância


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Gustavo', 'Cabral')
# p1.nome = 'Gustavo'
# p1.sobrenome = 'Cabral'


p2 = Pessoa('Lionel', 'Messi')
# p2.nome = 'Lionel'
# p2.sobrenome = 'Messi'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
