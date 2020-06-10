'''from random import randint
compu = randint(0,10)
print(compu)
cont = 1
num = int(input('Digite un número entre 1 y 10: '))
while compu != num:
    num = int(input('Por favor intente otro número: '))
    cont += 1

print('PARABÉNS!!!! Você acertou o número en su {}ª tentativa'.format(cont))'''

from random import randint
compu = randint(0,10)
print('Sou seu computador ...\nAcabei de pensar em um número entre 0 e 10')
print('Será que vpcÊ consegue adivinhar? ...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite un número: '))
    palpites += 1
    if jogador == compu:
        acertou = True
    else:
        if jogador < compu:
            print('Mais ... Tente de novo')
        else:
            print('Menos ... Tente de novo')

print('ACERTOU depois de {} tentativas'.format(palpites))