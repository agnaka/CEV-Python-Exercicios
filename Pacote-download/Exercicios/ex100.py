from random import randint
from time import sleep
print('=' * 50)
print(f'\033[1;34m{"EXERCÍCIO 100 - SORTÉIA|SOMA PAR":^50}\033[m')
print('=' * 50)
def sorteia():
    lista = list()
    for n in range(5):
        lista.append(randint(1,10))
    print(f'{"Sorteando 5 valores da lista:"}', end = '  ')
    for i in lista:
        print(f'{i}', end = ' ')
        sleep(0.3)
    print('PRONTO!')
    def somapar():
        par = 0
        for p in lista:
            if p % 2 == 0:
                par += p
        print(f'Somando os valores pares de {lista}, temos {par}')
    somapar()


sorteia()