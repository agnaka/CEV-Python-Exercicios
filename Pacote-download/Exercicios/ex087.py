matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
print('-=' * 20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 20)
print(f'A soma dos valores paes é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna {scol} ')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c]:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
print('FIM')

'''lista = []
par = []
maior2 = 0
for n in range(0, 3):
    lista.append(int(input(f'Digite um valor para [0, {n}]: ')))
for n in range(0, 3):
    lista.append(int(input(f'Digite um valor para [1, {n}]: ')))
for n in range(0, 3):
    lista.append(int(input(f'Digite um valor para [2, {n}]: ')))
print('-=' * 30)
print(f'[{lista [0]:^3}] [{lista [1]:^3}] [{lista [2]:^3}]')
print(f'[{lista [3]:^3}] [{lista [4]:^3}] [{lista [5]:^3}]')
print(f'[{lista [6]:^3}] [{lista [7]:^3}] [{lista [8]:^3}]')
print('-=' * 30)
for p in lista:
    if p % 2 == 0:
        par.append(p)
soma_par = sum(par)
for i in lista[3:6]:
    if i > maior2:
        maior2 = i

print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {lista[2] + lista[5] + lista[8]}')
print(f'O maior valor da segunda linha é {maior2}.')

print()
print('FIM')'''