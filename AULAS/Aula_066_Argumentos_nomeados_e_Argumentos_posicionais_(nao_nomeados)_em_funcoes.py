"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):         # Definicao de funcao 
    # Definicao
    print(f'{x=} y={y} z={z}', ' | ', 'x + y + z = ', x + y + z)

# Execucao de funcao 
soma(1, 2, 3)              # Argumento posicional   
soma(1, y=2, z=3)          # Argumento nomeado 

print(1, 2, 3, sep='-')
