# texto = 'Python s2'

# i = 0 
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i],i)

#     i += 1

'''Exemplo senha'''


# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laco acima pode ter repeticoes infinitas')

'''Exemplo FOR '''

texto = 'Python'

novo_texto = ''
for letra in texto: 
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')