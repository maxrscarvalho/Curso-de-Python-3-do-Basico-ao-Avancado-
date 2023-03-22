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

    def metodo_publico(self):
        return 'metodo_publico'

f = Foo()
print(f._protected)
# print(f.public())
# print(f.metodo_publico())