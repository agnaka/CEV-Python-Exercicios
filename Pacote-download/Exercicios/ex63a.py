num = int(input('Digite un numero: '))
cont = 3
if num == 1:
    print('0 -> FIM')
#    cont += 1
elif num == 2:
    print('0 -> 1 -> FIM')
#    cont += 1
soma_1 = 0
soma_2 = 1
while cont <= num:
    soma_1 = soma_1 + soma_2
    cont += 1
    print('{}'.format(soma_1), end=' -> ')
    if cont <= num:
        soma_2 = soma_2 + soma_1
        cont += 1
        print('{}'.format(soma_2), end=' -> ')

print('FIM')
