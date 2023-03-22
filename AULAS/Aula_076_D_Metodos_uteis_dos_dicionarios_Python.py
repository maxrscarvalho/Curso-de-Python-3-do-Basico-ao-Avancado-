'''Metodos uteis dos dicionarios em Python'''

# len - quantas chaves
# keys - iteravel com as chaves
# values - iteravel com os valores 
# items - iteravel com chaves e valores
# setdefault - adiciona valor se a chave nao existe
# copy - retorna uma copia rasa (shallow copy)
# get - obtem uma nova chave 
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga um ultimo item adicionado
# update - Atualiza um dicionario com outro 

import copy

d1 = {                          # shallow copy = copia rasa
    'c1' : 1,
    'C2' : 2,
    'l1' : [0, 1, 2],
}

d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999


print(d1)
print(d2)