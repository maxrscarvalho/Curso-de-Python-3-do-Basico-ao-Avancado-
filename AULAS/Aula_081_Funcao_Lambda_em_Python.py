
'''Funcao Lambda em Python'''

# A funcao lambda e uma funcao como qualquer outra em Python. Porem, sao funcoes anonimas que contem apenas uma lista. Ou seja, tudo deve ser contido dentro de uma unica expressao.


# O Sort ordena os itens dentro de uma lista.

lista = [
    {'nome': 'Max', 'Sobrenome': 'Carvalho'},
    {'nome': 'Maria', 'Sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'Sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'Sobrenome': 'Moreira'},
    {'nome': 'Aline', 'Sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista: 
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['Sobrenome'])

exibir(l1)
exibir(l2)