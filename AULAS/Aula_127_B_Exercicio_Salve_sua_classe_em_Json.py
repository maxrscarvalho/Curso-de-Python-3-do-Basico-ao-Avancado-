import json

from Aula_127_A_Exercicio_Salve_sua_classe_em_Json import caminho_arquivo, pessoa, fazer_dump

fazer_dump()

with open(caminho_arquivo, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = pessoa(**pessoas[0])
    p2 = pessoa(**pessoas[1])
    p3 = pessoa(**pessoas[2])

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

print(__name__)

if __name__ == '__main__':
    print('Ele e o Main')
    fazer_dump()