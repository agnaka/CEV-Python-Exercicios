from datetime import date
atual = date.today().year
cont_mais = 0
cont_menos = 0
for i in range(1, 8):
    n = int(input('Digite el año de nacimiento de la {}º persona: '.format(i)))
    if atual - n > 21:
        cont_mais += 1
    else:
        cont_menos += 1
print('{} personas son mayores de edad'.format(cont_mais))
print('{} personas son menores de edad'.format(cont_menos))

'''print('{} personas son mayores de edad'.format(cont))
print('{} personas son menores de edad'.format(7 - cont))'''
