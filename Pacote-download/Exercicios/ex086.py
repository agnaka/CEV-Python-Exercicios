matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
print()
print('FIM')
'''lista = [[], [], [], [], [], [], [], [], []]
for n in range(0,3):
    lista[n].append(int(input(f'Digite um valor para [0, {n}]: ')))
for n in range(3,6):
    lista[n].append(int(input(f'Digite um valor para [1, {n-3}]: ')))
for n in range(6,9):
    lista[n].append(int(input(f'Digite um valor para [2, {n-6}]: ')))
print('-=' * 30)
print(f'{lista[0]}{lista[1]}{lista[2]}\n{lista[3]}{lista[4]}{lista[5]}\n'
      f'{lista[6]}{lista[7]}{lista[8]}')'''

