"""import random
num = [0, 1, 2, 3, 4, 5]
num_1 = int(random.choice(num))
print(num_1)
num_e = int(input('Elija un número entre 0 y 5: '))
if num_1 == num_e:
    print('Adivinaste el número! FELICIACIONES!')
else:
    print('Lamentablemente no adivinaste el número que era {}'.format(num_1))"""

from random import randint
computador = randint(0, 5)
print('=' * 40)
print('ESTOU PENSANDO UM NÚMERO ENTRE O E 5 ......')
print('=' * 40)
jogador = int(input('Elija un número entre 0 y 5: '))
if jogador == computador:
    print('\033[1;4;34mADIVINASTE!!! el número era\033[m \033[1;35m"{}"\033[m! FELICIACIONES!'.format(computador))
else:
    print('\033[1;4;31mLamentablemente no adivinaste el número era\033[m \033[1;35m"{}"\033[m'.format(computador))
