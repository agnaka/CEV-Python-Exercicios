num = str(input('Digite un número entre 0 y 9999: '))
compri = len(num)
# print(compri)
if compri == 1:
    print('Unidade: {}'.format(num[0]))
elif compri == 2:
    print('Unidade: {}'.format(num[1]))
    print('Dezena: {}'.format(num[0]))
elif compri == 3:
    print('Unidade: {}'.format(num[2]))
    print('Dezena: {}'.format(num[1]))
    print('Centena: {}'.format(num[0]))
elif compri == 4:
    print('Unidade: {}'.format(num[3]))
    print('Dezena: {}'.format(num[2]))
    print('Centena: {}'.format(num[1]))
    print('Milhar: {}'.format(num[0]))
else:
    print('\033[1;33;42mUsted digitó un número de más de 4 dígitos\033[m')