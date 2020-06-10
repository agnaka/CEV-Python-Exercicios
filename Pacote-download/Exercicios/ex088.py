from random import randint
from time import sleep
print('-' * 30)
print(f'JOGA NA MEGA SENA'.center(30))
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 5, f'SORTEANDO {jogos} JOGOS', '-='* 5)
for sor in range(1,jogos+1):
    jogo = []
    for n in range(1, 7):
        num = randint(1, 60)
        if num in jogo:
            num = randint(1, 60)
        jogo.append(num)
    sleep(1)
    print(f'Jogo {sor}: {sorted(jogo)}')
print('-=' * 5, f'< BOA SORTE! >', '-=' * 5)
print()
print('FIM')