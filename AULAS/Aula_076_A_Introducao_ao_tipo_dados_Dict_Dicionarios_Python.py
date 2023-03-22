'''Dicionarios em Python (tipo dict)'''

# Dicionarios sao estruturas de dados tipo par de ''chave" e "Valor". 

# Chaves podem ser consideradas como o "Indice" que vimos na lista e podem ser de tipos imutaveis como: str, int, float, bool, tuple, etc.

# O valor pode ser de qualquer tipo, incluindo outro dicionario.

# Usamos as chaves - {} - ou a classe dict para criar dicionarios. 

# Imutaveis: str, int, float, bool, tuple

# mutavel: dict, list

pessoa = {
    'nome': 'Max Roberto',
    'Sobrenome': 'Carvalho',
    'Idade': 30, 
    'Altura': 1.8, 
    'Enderecos': [
        {'Rua': 'tal tal', 'numero': 123},
        {'Rua': 'Outra rua', 'numero': 321},
    ]
}
# pessoa = dict(nome='Max Roberto', sobrenome = 'Carvalho')
# print(pessoa, type(pessoa))

print(pessoa['nome'])
print(pessoa['Sobrenome'])

# print()


# for chave in pessoa:
#     print(chave, pessoa[chave])