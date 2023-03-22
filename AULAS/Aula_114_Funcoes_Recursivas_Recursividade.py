'''
Funcoes recursivas e recursividade
- funcoes que podem se chamar de volta 
- uteis para dividir problemas grandes em partes menores

Toda funcao recursia deve ter:
- Um problema que possa ser dividido em partes menores
- UM caso recursivo que resolve o pequeno problema 
- Um caso base que para a recursao
- fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
https://brasilescola.uol.com.br/matematica/fatorial.htm '''

# import sys 
# sys.setrecursionlimit(1004)               # cria um limite para o loop

# def recursiva(inicio=0, fim=10):

#     print(inicio, fim)
    
#     # Caso base
#     if inicio >= fim:
#         return fim

#     # Caso Recursivo
#     # Contar ate chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva(0, 1000))

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))
print(factorial(10))
print(factorial(100))



