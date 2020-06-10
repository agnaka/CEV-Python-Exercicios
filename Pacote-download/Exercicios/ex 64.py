print('\033[1;4;31mSOMA DE TODOS OS NÚMEROS DIGITADOS\033[m\n')
n1 = int(input('Digite um número: '))
n2 = 0
n3 = 0
cont = 0
while n1 != 999 and n2 != 999:
    n2 = int(input('Digite outro número: '))
    if n2 != 999:
        n3 = n1 + n2
        n1 = n3
    else:
        n3 = n1
    cont += 1
cuantos = cont
print(f'Você digitou {cuantos}')
print(f'A soma de todos os {cuantos} números digitados deu {n3}')
