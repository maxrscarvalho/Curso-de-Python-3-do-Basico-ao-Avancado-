import importlib

import Aula_098_m

print(Aula_098_m.variavel)

for i in range(10):
    importlib.reload(Aula_098_m)
    print(i)

print('Fim')