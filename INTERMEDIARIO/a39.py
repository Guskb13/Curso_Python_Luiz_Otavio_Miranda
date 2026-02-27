import importlib

import a39_m

print(a39_m.variavel)

for i in range(10):
    importlib.reload(a39_m)
    print(i)

print('Fim')