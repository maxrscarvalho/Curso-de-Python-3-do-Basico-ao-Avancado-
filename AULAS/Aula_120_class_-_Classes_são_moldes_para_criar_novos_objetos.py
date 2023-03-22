'''
Class - Classes sao moldes para criar novos objetos.

As classes geram novos objetos (instancias) que 
podem ter seus proprios atributos e metodos.

os objetos gerados pela classe podem usar seus dados 
internos para realizar varias acoes.

Por convencao, usamos PascalCase para nomes de classes.'''

# String = 'Max' # str.
# print(string.upper())
# print(isistance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Max','Carvalho')
# p1.nome = 'Max'
# p1.sobrenome = 'Carvalho'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)