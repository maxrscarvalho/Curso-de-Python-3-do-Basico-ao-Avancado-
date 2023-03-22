'''Manipulando chaves e valores em dicionarios'''


pessoa = {}

chave = 'nome'

pessoa[chave] = 'MAx Carvalho'
pessoa['sobrenome'] = 'Carvalho'

print(pessoa[chave])

pessoa[chave] = 'Joao'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome'):
    print('Nao Existe')
else: 
    print(pessoa['sobrenome'])