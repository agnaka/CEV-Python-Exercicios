from random import randint
print('=' * 30)
print(f'NÚMEROS ALEATÓRIOS'.center(30))
print('=' * 30)
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end = '')
for n in num:
    print(f'{n}', end = ' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor número sorteado foi {min(num)}')
print('-' * 30)
print('FIM')