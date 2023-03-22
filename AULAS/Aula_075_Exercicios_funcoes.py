'''Crie funcoes que duplicam, triplicam e quadruplicam o numero recebido como parametro.'''

'''Resolucao Max'''

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# numero = float(input('Digite um numero: '))
# print(duplicar(numero))
# print(triplicar(numero))
# print(quadruplicar(numero))

'''Resolucao Professor'''

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

numero = float(input('Digite um numero: '))

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)


print(duplicar(numero))
print(triplicar(numero))
print(quadruplicar(numero))