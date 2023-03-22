
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

pessoa = {
    'nome': 'Max Roberto',
    'Sobrenome': 'Carvalho',
    # 'idade': 990,
}

# print(len(pessoa))
# print(tuple(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# print(pessoa['idade'])
pessoa.setdefault('idade',0)


# for valor in pessoa.values():
    # print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)