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

class Foo:
    def __init__(self):             # O self referece a classe de instancia
        self.public = 'isso e publico'
        self._protected = 'isso e protegido'
        self.__exemplo = 'isso e private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self._protected)
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def _metodo_private(self):
        print('_metodo_private')
        return '_metodo_private'


f = Foo()
# print(f._protected)
# print(f.public())
print(f.metodo_publico())
print(f._Foo__metodo_private)