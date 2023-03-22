
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

