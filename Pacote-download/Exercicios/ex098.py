from time import sleep
print('=' * 40)
print(f'\033[1;32m{"EXERCÍCIO 097 - CONTADOR":^40}\033[m')
print('=' * 40)
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    if i < f:
        for n in range(i, f + 1, p):
            print(f'{n}', end =' ')
            sleep(.3)
    if i > f:
        for n in range(i, f - 1, -p):
            print(f'{n}', end =' ')
            sleep(.3)
    print('FIM!')
    print('-=' * 20)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
n1 = int(input(f'{"Inicio: ":<8}'))
n2 = int(input(f'{"Fim: ":<8}'))
n3 = abs(int(input(f'{"Passo: ":<8}')))
if n3 == 0:
    n3 = 0 + 1
print('-=' * 20)
contador(n1, n2 , n3)


