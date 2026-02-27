# Classes decoradoras (Decorator classes)
# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134


call_ = CallMe('23945876545')
call_('Lionel Messi')
retorno = call_('Luiz Otávio')
print(retorno)
