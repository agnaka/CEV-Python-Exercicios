p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão desta PA: '))
decimo = p + (10 - 1) * r
for i in range(p, decimo + r, r):
    print(i, end=" - ")
print('FIM')