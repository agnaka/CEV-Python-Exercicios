'''p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão desta PA: '))
decimo = p + (10 - 1) * r
for i in range(p, decimo + r, r):
    print(i, end=" - ")
print('FIM')'''

print('_' * 55)
print('PROJEÇÃO ARITMÉTICA \033[1m"PA"033[m - 10 PRIMEIROS NÚEMROS')
print('_' * 55)
p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão: '))
termo = p
cont = 1
while cont < 11:
    print('{}'.format(termo), end=' -> ')
    termo += r
    cont += 1
print('FIM')
