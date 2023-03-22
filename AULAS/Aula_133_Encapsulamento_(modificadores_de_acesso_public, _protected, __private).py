# Encapsulamento (modificadores de acesso: public, protected, private)
# python nao tem modificadores de acesso
# Mas podemos seguir as seguintes convecoes
#     (sem underline) = public
#         pode ser usado em qualuqer lugar
# _  (um underline) = protected
#         nao deve ser usado fora da classe
#         ou suas subclasses.
# __ (dois underlines) = private
#     "name mangling" (desconfiguracao de nomes) em python
#     so deve ser usado na classe em que foi declarado.

from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
# print(f.public)
print(f.metodo_publico())