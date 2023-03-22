frase = 'O paython e uma linguagem de progamacao ' \
    'multiparadigma.' \
    'Pyhton foi criado por Guido van Rossum. '.upper()

i = 0 
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len (frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

    print('A letra que apareceu mais vezes foi 'f'{letra_apareceu_mais_vezes} que apareceu 'f'{qtd_apareceu_mais_vezes}x')
