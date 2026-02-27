from abc import ABC, abstractmethod


class Conta(ABC):
    
    def __init__(self, Id_agencia: int, Id_conta: int):
        self._Id_conta = Id_conta
        self._Id_agencia = Id_agencia
        self._saldo = 0
        
    @abstractmethod
    def sacar(self, quantia: float) -> float:
        pass
    
    @abstractmethod
    def depositar(self, quantia):
        pass
    
    @property
    def Id_conta(self):
        return self._Id_conta
    
    @property
    def Id_agencia(self):
        return self._Id_agencia

    @Id_agencia.setter
    def Id_agencia(self, Id_agencia):
        self._Id_agencia = Id_agencia
      
    @property
    def saldo(self):
        return self._saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.Id_agencia!r}, {self.Id_conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'
    

class ContaCorrente(Conta):
    
    def __init__(self, Id_agencia, Id_conta):
        super().__init__(Id_agencia, Id_conta)
        self._bonus = True
        self._divida = 0
    
    def sacar(self, quantia):
        
        if self._saldo - quantia < 0 and self._bonus and quantia <= 100:
            print(f'Como você é um bom cliente vamos te dar um bonus de {quantia} reais a ser pago posteriormente!')
            self._bonus = False
            self._divida += quantia
            self._saldo = 0
            
        elif self._saldo - quantia < 0 and self._bonus and quantia > 100:
            print(f'Com um saldo de {self._saldo}, não é possível sacar {quantia}')
            print('Voce pode usar seu bonus, tente tirar uma quantia menor ou igual a 100')
            
        elif self._saldo - quantia < 0 and self._bonus is not True:
            print('Voce ja utilizou o seu bonus e após esse saque ficaria com saudo negativo')
            
            
        else:
            self._saldo -= quantia
            print(f'Saque realizado. Novo saldo: {self._saldo}')

            
                       
    def depositar(self, quantia):
        
        self._saldo = self._saldo + quantia
        
        if self._divida > 0 and self._saldo >= self._divida:
            print(f'Como seu saldo é maior que a divida, sua divida de {self._divida} reais foi paga')
            self._saldo -= self._divida
            self._divida = 0
            self._bonus = True  
        
        else:
            print(f'Depósito de {quantia} realizado. Novo saldo: {self._saldo}')
        
        
            
        
    @Conta.Id_agencia.setter
    def Id_agencia(self, Id_agencia):
        self._Id_agencia = Id_agencia
        
    @Conta.Id_conta.setter
    def Id_conta(self, Id_conta):
        self._Id_conta = Id_conta
    
    
class ContaPoupanca(Conta):
    
    def __init__(self, Id_agencia, Id_conta, ):
        super().__init__(Id_agencia, Id_conta)
    
    def sacar(self, quantia):
        if self._saldo - quantia < 0:
            print(f'Com um saldo de {self._saldo} reais, não é possível sacar {quantia} reais')
        else:
            self._saldo -= quantia
            print(f'Saque de {quantia} realizado. Novo saldo: {self._saldo}')
            
    def depositar(self, quantia):
        self._saldo += quantia
        print(f'Depósito de {quantia} reais realizado. Novo saldo: {self._saldo} reais')
        
        
    @Conta.Id_agencia.setter
    def Id_agencia(self, Id_agencia):
        self._Id_agencia = Id_agencia
        
    @Conta.Id_conta.setter
    def Id_conta(self, Id_conta):
        self._Id_conta = Id_conta

if __name__ == '__main__':
    # cp1 = ContaPoupanca(111, 222)
    # cp1.sacar(1)
    # cp1.depositar(1)
    # print(cp1.Id_conta)
    # print(cp1.Id_agencia)

    # print(cp1._saldo)
    # print('##')
    
    cc1 = ContaCorrente(111, 222)
    print(cc1._saldo)
    cc1.sacar(1)
    print(cc1._saldo)
    cc1.depositar(1)
    cc1.depositar(1)
    print(cc1._saldo)
    print(cc1.Id_conta)
    print(cc1.Id_agencia)
    print('##')
    