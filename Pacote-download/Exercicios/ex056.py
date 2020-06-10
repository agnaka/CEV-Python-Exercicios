from time import sleep
suma = 0
edad = 0
mayor = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1, 5):
    print('\033[1;4mDATOS DE LA {}ª PERSONA\033[m'.format(p))
    n = str(input('Digite el nombre de la persona: ')).strip()
    edad = int(input('Digite la edad de la persona: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    suma += edad
    if p == 1 and sexo in 'Mm':
        mayor = edad
        nomevelho = n
    if sexo in 'Mm' and edad > mayor:
        mayor = edad
        nomevelho = n
    if sexo in'Ff' and edad <20:
        totalmulher20 += 1
sleep(1)
media = suma / 4
print('\n\033[4mRESUMEN\033[m')
print('La media de las edades es de {}'.format(media))
print('El hombre mas viejo es {} y tiene {} anos'.format(nomevelho, mayor))
print('La cantidad de mujeres con menos de 20 anos es {}'.format(totalmulher20))
