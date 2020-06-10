"""import random
num = random.choice(range(1000, 2020))
print(num)"""
from datetime import date
num = int(input('Qué año querés saber si es bisiesto? Coloque 0 para el año actual: '))
if num == 0:
    print(date.today().year)
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print('\033[1;4;31mEl año\033[M \033[1;35m{}\033[m \033[1;4;31mes "BISIESTO"\033[m'.format(num))
else:
    print('\033[1;32mEl año \033[1;34m{}\033[m \033[1;32mno es "BISIESTO"\033[M'.format(num))
