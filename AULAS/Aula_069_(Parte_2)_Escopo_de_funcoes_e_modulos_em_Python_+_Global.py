
'''Escopo de funcoes em Python'''

'''Escopo significa o local onde aquele codifgo pode atingir.

Existe o escopo global e local.

O escopo global e aquele onde todo o codigo e alcancavel.
O escopo local e aquele onde apenas nomes do mesmo local podem ser alcancados.'''

x = 1           # Fora do escopo


def escopo():
    # global x             # Busca o valor de X fora da funcao (escopo) para que possa ser manipulada no escopo interno
    x = 10

    def outra_funcao():
        # global x        # Busca o valor de x fora da funcao (escopo) para que possa ser manipulada no escopo interno
        x = 11
        y = 2
        print(x,y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)            # Retorna o valor fora do escopo

