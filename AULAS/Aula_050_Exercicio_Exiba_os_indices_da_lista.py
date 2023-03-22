'''Exercicio

Exiba os indices da lista
0 Maria
1 Helena
2 Max'''

lista = ['Maria', 'Helena', 'Max']
indices = range(len(lista))                 # mostra a posicao do item na lista 


for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
  