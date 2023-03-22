# Yied from

def gen1():
    print('Comecou gen1')
    yield 1
    yield 2
    yield 3
    print('Acabou gen1')

def gen3():
    print('Comecou gen3')
    yield 10
    yield 20
    yield 30
    print('Acabou gen3')


def gen2(gen = None):
    print('Comecou gen2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('Comecou gen2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for numero in g1:
    print(numero)
print()

for numero in g2:
    print(numero)
print()

for numero in g3:
    print(numero)
print()