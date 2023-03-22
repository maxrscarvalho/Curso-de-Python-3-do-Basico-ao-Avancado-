'''Exercicios - Unir listas'''

'''Crie uma funcao zipper (como o zipper de roupas)
o trabalho dessa funcao sera unir duas listas na ordem
USe todos os valores da menor lista.

Ex.: 
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']

Resultado

[('Salvador','BA'), ('Ubatuba','SP'), ('Belo Horizonte', 'MG')]'''

# Resolucao 1

# def zipper(lista1,lista2):                                
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range (intervalo_maximo)
#     ]


# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(l1, l2))

# Resolucao 2

# A função zip() do Python cria um iterador que agregará elementos de dois ou mais iteráveis. Você pode usar o iterador resultante para resolver de forma rápida e consistente problemas comuns de programação, como a criação de dicionários.
# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip(l1, l2)))

# Resolucao 3

# from itertools import zip_longest
# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip_longest(l1, l2, fillvalue='Sem Cidade')))
