# Variaveis livres + nonlocal (locals, globals)

# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())                             # visualiza as funcoes dentro da variavel dentro 
#         print(dentro.__code__.co_freevars)          # visualiza as funcoes dentro da variavel dentro 
#         return a 
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

# print(globals())                    # opcoes de utlizar globals.

def concaternar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concaternar=''):
        nonlocal valor_final
        valor_final += valor_a_concaternar
        return valor_final
    return interna

c = concaternar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)


