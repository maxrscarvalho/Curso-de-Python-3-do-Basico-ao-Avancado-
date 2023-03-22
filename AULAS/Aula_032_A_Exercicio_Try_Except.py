'''Faca um programa que peca ao usuario para digitar um numero inteiro,
informe-se este numero e par ou impar. Caso o usuario nao digite um numero inteiro, informe que nao e um numero inteiro.''' 

'''Forma de resolver 1'''
 
#  entrada = input('Digite um numero: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'Impar'

#     if par_impar:
#         par_impar_texto = 'par'
#         print('O numero {} e {}'.format(entrada_int, par_impar_texto))

# else: 
#     print('Voce nao digitou um numero inteiro')

'''Forma de resolver 2'''

entrada = input('Digite um numero: ')

try:

    
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Impar'

    if par_impar:
        par_impar_texto = 'par'
        print('O numero {} e {}'.format(entrada_int, par_impar_texto))

except: 
    
    print('Voce nao digitou um numero inteiro')