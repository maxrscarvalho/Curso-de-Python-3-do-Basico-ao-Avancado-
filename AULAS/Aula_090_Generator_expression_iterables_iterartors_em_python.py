# Generator expression, Iterables e Iterators em python.

# iterable = ['Eu', 'Tenho', '_iter_']
# iterator = iter(iterable)          # tem _iter_e_next_

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

'''Generator'''

import sys

iterable = ['Eu', 'Tenho', '_iter_']
iterator = iter(iterable)          # tem _iter_e_next_
lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(len(generator))

# for n in generator:
#     print(n)