# __dict__ e vars para atributos de instancia 

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = Pessoa('Joao', 35)
p1 = Pessoa(**dados)
# p1.nome = 'eita'
# del p1.nome
# print(p1.nome)
# p1.__dict__['Outra'] = 'coisa'
# p1.__dict__['Nome'] = 'eita'

# del p1.__dict__['Nome']

# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)

print(vars(p1))