print('\033[1;4;31mSOMA DE TODOS OS NÚMEROS DIGITADOS\033[m\n')
# n1 = int(input('Digite um número: '))
n1 = 0
n3 = 0
cont = 0
while n1 != 999 :
    n1 = int(input('Digite outro número: '))
    if n1 != 999:
        n3 += n1
 #       n1 = n3
        cont += 1
cuantos = cont
print(f'Você digitou {cuantos}')
print(f'A soma de todos os {cuantos} números digitados deu {n3}')