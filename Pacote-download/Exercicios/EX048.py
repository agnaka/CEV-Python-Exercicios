s = 0
cont = 0
for i in range(1, 501, 2):
        if i % 3 == 0:
            s += i
            cont += 1
print('A soma dos {} ímpares entre 1 e 500 é: {}'.format(cont, s))
print('FIM')