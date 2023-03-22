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


p1 = {
    'nome': 'Max',
    'sobrenome': 'Carvalho',
}

# print(p1['nome'])
# print(p1.get('nome', 'Nao existe'))


# nome = p1.pop('nome')
# print(nome)
# print(p1)


# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'idade': 30,
# })
# print(p1)

# p1.update(nome = 'novo valor', idade = 30)
# tupla = (('nome', 'novo valor'), ('idade',  30))
lista = [['nome', 'novo valor'], ['idade' ,30]]
p1.update(lista)
print(p1)