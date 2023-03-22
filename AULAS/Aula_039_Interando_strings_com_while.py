'''Interando Strings com While'''
#       012345678910
# nome = 'Max Carvalho' # Interaveis
#       111098745321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

nome = 'Max Carvalho' # Interaveis 
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)