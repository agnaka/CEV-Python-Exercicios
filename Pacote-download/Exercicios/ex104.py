print('=' * 40)
print(f'\033[1;36m{"EXERCÍCIO 104 - Função LEIANT":^40}\033[m')
print('=' * 40)
def leaint(n):
    if n.isnumeric():
        n = int(n)
    else:
        print('\033[31mERRO! Digite um número inteiro válido\033[m')
        n = leaint(input('Digite um número: '))
    return (n)

# Programa Principal
n = leaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}.')

'''def leaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')'''