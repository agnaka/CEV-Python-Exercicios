from random import randint
from time import sleep
jogador = {}
jogador_max = {}
lista = []
lista_max = []
cont = max = 0
print('Valores sorteados:')
for j in range(0,4):
    cont += 1
    jogador['jogador'] = f'{cont}'
    jogador['tirou'] = randint(1,6)
    lista.append(jogador.copy())
    print(f'   O jogador{lista[cont-1]["jogador"]} tirou {lista[cont-1]["tirou"]}')
    sleep(1)
print('Ranking dos jogadores:')
sleep(2)
print()
for m in range(0, 4):
    if m == 0:
        lista_max.insert(0, lista[m])
    else:
        pos = 0
        while pos <= len(lista_max):
            if pos == len(lista_max):
                lista_max.append(lista[m])
                break
            if lista[m]['tirou'] >= lista_max[pos]['tirou']:
                lista_max.insert(pos, lista[m])
                break
            pos += 1
# print(lista_max)
for p in range(0, 4):
    print(f'   {p + 1}ª lugar: jogador{lista_max[p]["jogador"]} com {lista_max[p]["tirou"]}')
    sleep(1)
print()
print('FIM')
