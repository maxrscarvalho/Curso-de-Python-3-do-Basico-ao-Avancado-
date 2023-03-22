'''Exemplo 1'''

string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string [i]

    if letra == ' ':
        break

    print(letra)
    i += 1

else: 
    print('Nao encontrei um espaco na string')    # O else foi executado
print('Fora do while.')       # Fora do while 