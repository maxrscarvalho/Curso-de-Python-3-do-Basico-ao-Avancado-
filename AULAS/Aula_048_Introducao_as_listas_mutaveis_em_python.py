'''LISTAS EM PYTHON'''

'''Tipo list - Mutavel'''

'''Suporta varios valores de qualquer tipo 
Conhecimentos reutilizaveis  - indices e fatiamento
Metodos Uteis: append, insert, pop, del, clear, extend, +
'''

#       01234
#      -54321

# string = 'ABDCE'  # 5 caracteres # tambem posso usar (len)
# lista = [123, True, 'Max', 1.2, []]        # Tambem pode ser usado list()
# # print(bool(lista))   # se a lista estiver vazia ela e falsy
# # print(lista, type(lista))
# print(lista)

'''Exemplo - trocar itens dentro de uma lista'''

#        0    1      2     3    4
#       -5   -4    -3    -2   -1
# lista = [123, True, 'Max', 1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))


# Create Read Update   delete   (CRUD)
# criar  ler  alterar  apagar

#          0    1   2   3  
# lista = [10 , 20, 30, 40]
# lista[2] = 300
# del lista[2]       # O comando del tem a funcao de deletar / # o [2] indica a posicao do item na lista que deseja deletar
# print(lista)
# print(lista[2])

# lista.append(50)     # O comando (.append) ele tem a funcao de adicionar itens no final da lista ja declarada
# lista.pop()          # O comando (.pop()) remove o ultimo item da lista 
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)             # com o comando (.pop(3)) deleta o item na posicao 3 da lista
# print(lista, 'Removido', ultimo_valor)

'''Segunda Aula sobre Listas '''

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#          0   1   2   3
# lista = [10, 20, 30, 40]
# lista.append('Max')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(100, 5)
# print(lista[4])

# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_a)


'''Terceira Aula sobre listas - Cuidados'''

'''cuidados co dados mutaveis 
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel) '''

lista_a = ['max','carvalho', True, 1, 2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)