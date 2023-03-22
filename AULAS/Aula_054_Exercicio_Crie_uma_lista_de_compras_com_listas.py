'''Faca uma lista de comprar com listas o usuario deve ter a possibilidade de inserir, apagar
e listar valores da sua lista. Nao permita que o programa quebre com erros de indices existentes na lista. '''


import os 

lista = []
while True: 
    print('Selecione um opcao')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    
    elif opcao == 'a':
        indice_str = input(
            'Escolha o indice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        
        except ValueError: 
            print('Nao foi possivel apagar este indice')

        except IndexError:
            print('Indice nao existe na lista')

        except Exception: 
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i,valor)
    else:
        print('Por favor, escolha i, a ou l.')