from conta import ContaCorrente, ContaPoupanca, Conta
from pessoa import Cliente, Pessoa


class Banco:
    def __init__(
        self,
        nome, 
        Id_banco,
        agencias: list[int] | None = None,
        clientes: list[Cliente] | None = None,
        contas: list[Conta] | None = None,
    ):
        
        self._nome = nome
        self._Id_banco = Id_banco
        self._agencias = agencias or []
        self._clientes = clientes or []
        self._contas = contas or []
        
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self._nome!r}, {self._Id_banco!r}, {self._agencias!r},\
            {self._clientes!r}, {self._contas!r})'
        return f'{class_name}{attrs}'
        
    def criar_agencia(self, agencias):
        for agencia in agencias:
            self._agencias.append(agencia)
            
    def listar_agencias(self):
        print()
        for agencia in self._agencias:
            print(agencia)
        
    
    def criar_cliente(self, pessoa):
        cliente = Cliente(
            pessoa._nome,
            pessoa._cpf,
            pessoa._idade,
        )

        self._clientes.append(cliente)
        return cliente
    
    def criar_conta(self, cliente, Id_agencia, Id_conta, tipo):

        if cliente not in self._clientes:
            print("Cliente não pertence a este banco")
            return

        if Id_agencia not in self._agencias:
            print("Agência não existe")
            return

        if tipo == "corrente":
            conta = ContaCorrente(Id_agencia, Id_conta)

        elif tipo == "poupanca":
            conta = ContaPoupanca(Id_agencia, Id_conta)

        else:
            print("Tipo inválido")
            return

        self._contas.append(conta)
        return conta




    def autenticar(self, cliente : Cliente, conta: Conta):
        if cliente not in self._clientes:
            print("Cliente não pertence ao banco")
            return False

        if conta not in self._contas:
            print("Conta não pertence ao banco")
            return False

        if conta.Id_agencia not in self._agencias:
            print("Agência inválida")
            return False
        
        if conta is not cliente._conta_corrente and conta is not cliente._conta_poupanca:
            return False

        return True
    
    
    
    def sacar(self, cliente, conta, valor):
        if self.autenticar(cliente, conta):
            conta.sacar(valor)
            
            
            
    def depositar(self, cliente, conta, valor):
        if self.autenticar(cliente, conta):
            conta.depositar(valor)


if __name__ == '__main__':
    
    c1 = Cliente('Gustavo', '234653234-45', 21)
    c2 = Cliente('Vitor', '123123123-12', 26)
    cc1 = ContaCorrente(111, 222)
    cc2 = ContaCorrente(112,223)
    
    c1._conta_corrente = cc1
    c2._conta_corrente = cc2
    
    banco1 = Banco('Santander', 1)
    banco1._clientes.extend([c1, c2])
    banco1._contas.extend([cc1, cc2])
    banco1._agencias.extend([111, 112])
    print(banco1.autenticar(c2,cc2))
    
    print(banco1)
    
    banco1.depositar(c1, cc1, 100)
    print(cc1)

    

