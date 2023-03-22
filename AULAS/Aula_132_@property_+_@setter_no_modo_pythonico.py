'''
@property + @setter - getter e setter no modo Pythonico

- Como Getter.
- Para evitar quebrar codigo cliente.
- Para habilitar setter.
- Para Executar acoes ao obter um atributo
- Atributos que comecem com um ou dois underlines.
- Nao devem ser usados fora da classe. '''


class Caneta:
    def __init__(self, cor):
        # private protected 
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('Estou no getter')
        return self._cor

    @cor.setter
    def cor(self, valor):
        # if valor == 'Rosa':
        #     raise ValueError('Nao aceito essa cor')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


# def mostrar(caneta):
#     return caneta.cor

caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'

# Getter -> obter valor
print(caneta.cor)
print(caneta.cor_tampa)