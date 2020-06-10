"""import math
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
hipo = math.sqrt((math.pow(c1, 2) + math.pow(c2, 2)))
print('O comprimento da hipotenusa é {:.2f}'.format(hipo))"""

from math import hypot
co = float(input('\033[4mDigite o valor do cateto oposto:\033[m '))
ca = float(input('\033[1mDigite o valor do cateto adjacente:\033[m '))
hi = hypot(co, ca)
print('\033[1;4mA hipotenusa vai medir\033[m \033[1;37m{:.2f}\033[m'.format(hi))