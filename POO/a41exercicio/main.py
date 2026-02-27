from banco import Banco
from pessoa import Pessoa, Cliente
from conta import ContaCorrente, ContaPoupanca


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