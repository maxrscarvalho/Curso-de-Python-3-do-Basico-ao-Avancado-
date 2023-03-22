
'''Empacotamento e Desempacotamento de dicionarios'''


"Pacotamento"


# a, b = 1, 2
# a, b = b, a
# print(a,b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)


# for chave, valor in pessoa.items():
#     print(chave, valor)


# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)

"""Desempacotamento"""


# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }

# dado_pesssoa = {
#     'idade':  30,
#     'altura': 1.85,
# }

# pessoa_completa = {**pessoa, 'nome': 1}


# print(pessoa_completa)

'''Exemplo 3'''

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade':  30,
    'altura': 1.85,
}

pessoa_completa = {**pessoa,**dados_pessoa}

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NAO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1,2, nomee='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}

mostro_argumentos_nomeados(**configuracoes)