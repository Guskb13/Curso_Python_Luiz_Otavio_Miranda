from abc import ABC, abstractmethod
from conta import Conta, ContaCorrente, ContaPoupanca

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, idade: int): 
        self._nome = nome
        self._cpf = cpf
        self._idade = idade
                
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def idade(self):
        return self._idade
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.cpf!r}, {self.idade!r})'
        return f'{class_name}{attrs}'
        
        
        
        
class Cliente(Pessoa):
    
    def __init__(self, nome, cpf, idade):
        super().__init__(nome, cpf, idade)  
        
        self._conta_corrente: Conta | None = None
        self._conta_poupanca: Conta | None = None
        
    def mostrar_contas(self):
        
        if self._conta_corrente is not None:
            print(self._conta_corrente)
        if self._conta_poupanca is not None:
            print(self._conta_poupanca)
        
           
           
           
if __name__ =='__main__':
    c1 = Cliente('Gustavo', '234653234-45', 21)
    print(c1) 
    c1._conta_corrente = ContaCorrente(111, 222)
    c1.mostrar_contas() 
    print(c1._conta_corrente)
    c2 = Cliente('Vitor', '123123123-12', 26)
    c2._conta_corrente = ContaCorrente(111,223)
    print(c2)
    print(c2._conta_corrente)