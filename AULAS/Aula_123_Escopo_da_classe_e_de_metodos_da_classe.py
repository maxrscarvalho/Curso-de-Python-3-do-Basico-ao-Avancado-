# Escopo da classe e de metodos da classe.

class Animal:
    nome = 'Leao'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} esta comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        self.comendo(*args, **kwargs)


leao = Animal(nome='Leao')
print(Animal.nome)
print(leao.comendo('maca'))