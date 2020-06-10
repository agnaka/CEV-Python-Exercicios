exp = input('Digite a expressão: ')
cont_1 = cont_2 = 0
for i in exp:
    if i == '(':
        cont_1 += 1
    if i == ')':
        cont_2 += 1
        if cont_2 > cont_1:
            break
if cont_1 == cont_2:
    print('CORRETO')
else:
    print('\033[1;31mERRADO!!!\033[m')

print('\nFIM')