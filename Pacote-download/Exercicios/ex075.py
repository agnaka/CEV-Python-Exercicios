print('-' * 30)
print(f'EXERCÍCIOS DE TUPLAS #075'.center(30))
print('-' * 30)
n1 = int(input('Digite un número: '))
n2 = int(input('Digite otro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o últinmo número: '))
num = (n1, n2, n3, n4)
print('-' * 25)
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 not in num:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
print('Os valores pares digitados foram', end = ' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end =' ')
print('\nFIM')


