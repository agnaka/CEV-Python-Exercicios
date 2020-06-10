n1 = int(input('\033[31mDigite un número entero:\033[m '))
n2 = int(input('\033[32mDigite otro número entero:\033[m '))
n3 = int(input('\033[33mDigite el último número entero:\033[m '))

"""lista = [n1, n2, n3]
lista_1 = lista.sort()
print('Este es el número menor: {}'.format(lista[0]))"""

if n1 > n2 and n1 >n3:
    print('El número {} es el mayor'.format(n1))
if n2 > n1 and n2 > n3:
        print('El número {} es el mayor'.format(n2))
if n3 > n1 and n3 > n2:
        print('El número {} es el mayor'.format(n3))

if n1 < n2 and n1 < n3:
    print('El número {} es el menor'.format(n1))
if n2 < n1 and n2 < n3:
    print('El ´numero {} es el menor'.format(n2))
if n3< n1 and n3 < n2:
    print('El número {} es el menor'.format(n3))