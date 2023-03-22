'''Groupby - Agrupar por'''
from itertools import groupby

alunos = [
    {'Nome': 'Luiz', 'nota':'A'},
    {'Nome': 'Leticia', 'nota':'B'},
    {'Nome': 'Fabricio', 'nota':'A'},
    {'Nome': 'Rosemary', 'nota':'C'},
    {'Nome': 'Joana', 'nota':'D'},
    {'Nome': 'Joao', 'nota':'A'},
    {'Nome': 'Eduardo', 'nota':'B'},
    {'Nome': 'Andre', 'nota':'A'},
    {'Nome': 'Anderson', 'nota':'C'},
]


def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))
    for aluno in grupo:
        print(aluno)

# grupos = groupby(alunos)

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))