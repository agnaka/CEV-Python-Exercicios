print('=' * 20)
num = int(input('Digite un número: '))
print('=' * 20)
print('El doble del número digitado es \033[32m{}\033[m \nEl triple es \033[1;34m{}\033[m \nEl cuadrado es \033[1;32;45m{}\033[m'.format(num *2, num * 3, num**2))

