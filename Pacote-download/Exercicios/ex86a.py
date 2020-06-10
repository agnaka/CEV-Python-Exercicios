lista = []
for n in range(0, 3):
    lista.append(int(input(f'Digite um valor para [0, {n}]: ')))
for n in range(0, 3):
    lista.append(int(input(f'Digite um valor para [1, {n}]: ')))
for n in range(0, 3):
    lista.append(int(input(f'Digite um valor para [2, {n}]: ')))
print('-=' * 30)
print(f'[ {lista [0]} ] [ {lista [1]} ] [ {lista [2]} ]')
print(f'[ {lista [3]} ] [ {lista [4]} ] [ {lista [5]} ]')
print(f'[ {lista [6]} ] [ {lista [7]} ] [ {lista [8]} ]')
print()
print('FIM')
