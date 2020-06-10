s = 0
c = 0
for i in range(1,7):
    n = int(input('Digite o {}º número: '.format(i)))
    if n % 2 == 0:
        s += n
        c = c + 1
print('{} números pares de los digitados son pares y la suma es {}'.format(c, s))