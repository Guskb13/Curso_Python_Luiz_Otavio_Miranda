# Exercicios
# Crie funções que duplicam, triplicam, e quadriplicam
 # o número recebido como parâmetro
 
def aumenta(multiplicador):
    def valor_que_aumenta(numero):
        return multiplicador * numero
    return valor_que_aumenta

duplicar = aumenta(2)
triplicar = aumenta(3)
Vezes4 = aumenta(4)

print(duplicar(3))
print(triplicar(3))
print(Vezes4(3))
        