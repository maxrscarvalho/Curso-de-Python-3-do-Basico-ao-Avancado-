"""
Introucao ao try/except
try -> tentar executar o codigo 
except -> ocorreu algum erro ao tentar executar
"""
numero = input ('vou dobrar o numero que vc digitar: ')

try:
    print ('STR:', numero_str)
    numero_float = float (numero_str)
    print ('FLOAT:', numero_float)
    print (f'o dobro de {numero_str} e {numero_float * 2: }')

except:
    print ('Isso nao e um numero')


# if numero_str.isdigit():
#     numero_float = floar (numero_str)
#     print (f'o dobro de {numero_str} e {numero_float * 2:}')

# else:
#     print ('Isso nao e um numero')
