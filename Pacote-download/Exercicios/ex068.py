from random import randint
print('=-' * 20)
print('\033[1;4;36mVAMOS A JOGAR PAR OU IMPAR!!!\033[m')
print('=-' *20)

cont = 0
while True:
    num = int(input('Digite um valor: '))
    pi = str(input('Par ou Impar? [P/I] ')).strip().upper()
    while pi not in "PI":
        pi = str(input('Par ou Impar? [P/I] ')).strip().upper()
    compu = randint(1, 2)
#    print(compu)
    soma = num + compu
    if pi == "P" and soma % 2 == 0:
        print(f"Você jogou {num} e o computador {compu}. Total de {soma} DEU PAR")
        print('Você VENCEU!\nVamos jogar novamente ...')
        print('--' * 12)
    elif pi == 'I' and soma % 2 != 0:
        print(f"Você jogou {num} e o computador {compu}. Total de {soma} DEU IMPAR")
        print('Você VENCEU!\nVamos jogar novamente ...')
        print('--' * 12)
    else:
        print(f'GAME OVER! Você venceu {cont} vezes!')
        print('--' * 12)
        break

    cont += 1
print('FIM')



