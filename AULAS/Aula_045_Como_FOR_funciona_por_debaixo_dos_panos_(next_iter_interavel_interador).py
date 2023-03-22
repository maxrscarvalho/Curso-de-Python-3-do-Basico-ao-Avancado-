'''
Iteravel -> str, range, etc (____iter____)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor 
iter -> me entregue seu iterador'''

'''Exemplo 1'''

# texto = 'Max'
# numeros  = range(0, 100, 8)

# for numero in numeros: 
#     print(numero)

'''Exemplo 2'''

# for letra in texto
texto = 'Max' # iteravel
iteratador = iter(texto) # ietardor

while True: 
    try: 
        print(next(iteratador))
    except StopIteration:
        break

