'''
Combinacao - Ordem nao importa - iteravel + tamanho do grupo.
Permutacao - ordem importa 
Produto - Ordem importa e repete valores unicos '''

from itertools import combinations
from itertools import permutations
from itertools import product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'Joao', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'G'],
    ['masculino', 'femino', 'unissex'],
    ['algodao', 'poliester'],
    
]


# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
