from time import sleep
print('=' * 40)
print(f'\033[1;32m{"EXERCÍCIO 099 - MAIOR":^40}\033[m')
print('=' * 40)
def maior(*num):
    print('Analisando os valores passados ...')
    grande = 0
    for n in num:
        print(f'{n}', end= ' ')
        sleep(.3)
        if n > grande:
            grande = n
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {grande}.')
    print('-=' * 30)


print('FIM!')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
maior()
