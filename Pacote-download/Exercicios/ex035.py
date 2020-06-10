"""r1 = float(input('Digite o comprimento de um segmento: '))
r2 = float(input('Digite o comprimento de outro segmento: '))
r3 = float(input('Digite o comprimento do último segmento:  '))
lista = [r1, r2, r3]
lista.sort()

# print(lista[0] * lista[1])
print(lista)
if (float(lista[0]) * float(lista[0]) + float(lista[1]) * (float(lista[1])) == float(lista[2]) * float(lista[2])):
    print('\033[1;35mEstes 3 segmentos\033[m \033[1;32m{}, {} e {}\033[m \033[1;35mpodem formar um triángulo retángulo\033[m'.format(lista[0], lista[1], lista[2]))
else:
    print('\033[1;4;31;40mEstos 3 segmentos não podem formar um triángulo retângulo\033[m')"""
print('-='*20)
r1 = float(input('Digite o comprimento de um segmento: '))
r2 = float(input('Digite o comprimento de outro segmento: '))
r3 = float(input('Digite o comprimento do último segmento:  '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os segmentos acima POPDEM FORMAR TRIÁNGULO')
else:
    print('Os segmentos acima NÃO POPDEM FORMAR TRIÁNGULO')
