# Exercicio - Salve sua classe em Json
# Salve os dados da sua classe em Json
# E depois crie novamente as instancias 
# da classe com os dados salvos
# Faca em arquivos separados.


# Pessoas= ['Maria', 'Joao', 'Carlos', 'Jose', 'Renan', 'Ricardo']
# Pessoas.append('Josefina')
# Pessoas.remove('Maria')
# print(Pessoas)
# for count, valor in enumerate (0, 5):
#     print(Pessoas)

import json

caminho_arquivo = 'aula127.json'

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = pessoa('Joao', 32)
p2 = pessoa('Helena', 21)
p3 = pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__,vars(p3)]

def fazer_dump():

    with open(caminho_arquivo, 'w') as arquivo:
        print('Fazendo Dump')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
