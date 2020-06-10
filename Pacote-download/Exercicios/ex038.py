print('\033[1mVAMOS A COMPARAR 2 NÚMEROS INTEIROS\033[m')
num_1 = int(input('Digite o primeiro número inteiro: '))
num_2 = int(input('Digite o segundo número inteiro: '))
if num_1 > num_2:
    print('El primer número \033[1;35m{}\033[m é maior que o segundo número \033[1;35m{}\033[m'.format(num_1, num_2))
elif num_2 > num_1:
    print('El segundo número \033[1;35m{}\033[m é maior que o primeiro número \033[1;35m{}\033[m'.format(num_2, num_1))
else:
    print('O primeiro e o segundo número são iguais!!!')