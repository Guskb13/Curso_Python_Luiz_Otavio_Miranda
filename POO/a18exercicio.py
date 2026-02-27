# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor
        valor.inserir_carros(self)
        
    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        valor.inserir_carros(self)
        
    def mostrar_carro(self):
        print(f'Carro: {self.nome}')

        if self.motor:
            print(f'Motor: {self.motor.nome}')
        else:
            print('Motor: não definido')

        if self.fabricante:
            print(f'Fabricante: {self.fabricante.nome}')
        else:
            print('Fabricante: não definido')
            
        print()

            
class Motor:
    def __init__(self, nome):
        self.nome = nome
        self._carros = []
        
    def inserir_carros(self, *carros):
        for carro in carros:
            if carro not in self._carros:
                self._carros.append(carro)

            
    def listar_carros(self):
        print(f'O motor {self.nome} está nos carros')
        for carro in self._carros:
            print(carro.nome)
        print()

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._carros = []
        
    def inserir_carros(self, *carros):
        for carro in carros:
            if carro not in self._carros:
                self._carros.append(carro)

            
    def listar_carros(self):
        for carro in self._carros:
            print(f'A fabricante {self.nome} fabricou os carros')
            print(carro.nome)
        print()
             
        
Chevrolet = Fabricante('Chevrolet')
Ford = Fabricante('Ford')
ferrari = Fabricante('Ferrari')

V8 = Motor('v8')
V8_turbo = Motor('v8 turbo')

ford_cobra = Carro('Ford Cobra')
chevrolet_chevelle = Carro('Chevrolet Chevelle')
ferrari_enzo = Carro('Ferrari Enzo')

ford_cobra.fabricante = Ford
chevrolet_chevelle.fabricante = Chevrolet
ferrari_enzo.fabricante = ferrari

ford_cobra.motor = V8
chevrolet_chevelle.motor = V8_turbo
ferrari_enzo.motor = V8_turbo

ford_cobra.mostrar_carro()
chevrolet_chevelle.mostrar_carro()
ferrari_enzo.mostrar_carro()

V8_turbo.listar_carros()
Chevrolet.listar_carros()
