'''Repeticoes

While (enquanto)''' #Executa uma condicao for verdeira 
# loop infinito = Quando um codigo nao tem fim

'''Exemplo 1'''

contador = 0

while contador <= 100:
    contador += 1 
    
    if contador == 6:
        print('Nao vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Nao vou mostrar o', contador)
        continue

        break

print('Acabou')