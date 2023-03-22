# while True:
#     sair = input('Quer sair? [s]im ')
#     sair = sair.lower()
#     sair = sair.startswith('s')

#     print(sair)

'''exemplo 2 - Calculadora'''

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um numero (+-/*): ')
    numeros_validos = True

    try: 
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
         
    except:
        numeros_validos is None

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados sao invalidos.')
        continue

    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len (operador) > 1:
        print('Operador invalido')
        continue

    print('Realizando sua conta. Confira o resultado abaixo: ')

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} =', numero_1_float + numero_2_float)

    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} =', numero_1_float - numero_2_float)

    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float} =', numero_1_float / numero_2_float)

    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float} =', numero_1_float * numero_2_float)

    else: 
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im ').lower().startswith('s')

    if sair is True: 
        break
    
    