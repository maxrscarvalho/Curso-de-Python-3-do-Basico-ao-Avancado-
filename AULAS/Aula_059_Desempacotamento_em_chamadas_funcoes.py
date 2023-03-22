'''Desempacotamento em chamadas'''

# De Metodos e funcoes 

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'e', 'Legal'
salas = [
 'ABCD'
'Maria', 'Helena', 1, 2, 3, 'Eduarda'
 'Python', 'e', 'Legal'
]
# p, b, *_, ap, u = lista
# print(p,u,ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')