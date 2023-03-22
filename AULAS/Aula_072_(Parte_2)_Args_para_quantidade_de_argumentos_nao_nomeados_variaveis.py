
'''args - Argumentos nao nomeados'''

''' *- *args (empacotamento e desempacotamento)'''

# Semper se lembrar do desempacotamento


# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma (x, y):
#         return x + y

# def soma(*args):
#     # print(args)
#     total = 0
#     for numero in args: 
#         total = total + numero
#     return total


# soma_1_2_3 = soma(1, 2, 3)
# # print(soma_1_2_3)

# soma_4_5_6 = soma(4, 5, 6)
# # print(soma_4_5_6)

# numeros  = 1,2,3,4,5,6,7,78,10
# outra_soma = soma(*numeros)         # (*numeros) o asteristicos serve com funcao de desempacotador 
# print(outra_soma)

# # print(sum((1,2,3,4,5,6,7,78,10)))
# print(*numeros)




'''Exercicio com funcoes'''

# Crie uma funcao que multiplica todos os argumentos nao nomeados recebidos. Retorne o valor da vriavel. 

def multiplicar (*args):
    total = 1
    for numero in args: 
        total *= numero
    return total 

multiplication = multiplicar(1,2,3,4,5)
print(multiplication)


# Crie uma funcao se um numero e par ou impar. Retorne se o numero e par ou impar.

def par_impar(numero):
    return numero % 2  == 0

    if multiplo_de_dois:
        return f'{numero} e Par'
        return f'{numero} e impar'          # Else e redudante no codigo 

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))