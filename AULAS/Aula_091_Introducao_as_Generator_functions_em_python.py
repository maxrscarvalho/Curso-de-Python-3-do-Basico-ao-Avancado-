# Introducao as Generator function em Python.
# generator = (n for n in range (1000000))

'''Exemplo 1'''

# def generator(n = 0):
#     yield 1           # Pausar
#     print('Continuando')
#     yield 2            # Pausar
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar')
#     return 'Acabou'

# gen = generator(n = 0)
# print(next(gen))
# for n in gen:
#     print(n)

'''Exemplo 2'''

def generator(n=0, maximum=10):
    while True: 
        yield n
        n += 1

        if n >= maximum: 
            return

gen = generator(maximum=1000)
for n in gen: 
    print(n)
