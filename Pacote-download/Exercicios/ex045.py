from random import randint
print('-=' * 20)
print('\033[1;34mVAMOS A JOGAR JANKENPÔ!!!\033[m')
print('-=' * 20)
print('''SUAS OPÇÕES:
[1] Pedra
[2] Papel
[3] Tesoura''')
choice = int(input('Qual a sua escolha? '))
print('JAN')
print('KEN')
print('PO!!!')
itens = ('Pedra', 'Papel', 'Tesoura')
compu = randint(1, 3)
# print(compu)
if compu == 1 and choice == 1:
    print('O computador escolheu {} e você {} - EMPATOU! Jogar novamente'.format('PEDRA', 'PEDRA'))
elif compu == 1 and choice == 2:
    print('O computador escolheu {} e você {} - VOCÊ GANHOU!!!'.format('PEDRA', 'PAPEL'))
elif compu == 1 and choice == 3:
    print('O computador escolheu {} e você {} - VOCÊ PERDEU'.format('PEDRA', 'TESOURA'))
elif compu == 2 and choice == 2:
    print('O computador escolheu {} e você {} - EMPATOU! Jogar novamente'.format('PAPEL', 'PAPEL'))
elif compu == 2 and choice == 1:
    print('O computador escolheu {} e você {} - VOCÊ PERDEU'.format('PAPEL', 'PEDRA'))
elif compu == 2 and choice == 3:
    print('O computador escolheu {} e você {} - VOCÊ GANHOU!!!'.format('PAPEL', 'TESOURA'))
elif compu == 3 and choice == 3:
    print('O computador escolheu {} e você {} - EMPATOU! Jogar novamente'.format('TESOURA', 'TESOURA'))
elif compu == 3 and choice == 1:
    print('O computador escolheu {} e você {} - VOCÊ GANHOU!!!'.format('TESOURA', 'PEDRA'))
elif compu == 3 and choice == 2:
    print('O computador escolheu {} e você {} - VOCÊ PERDEU'.format('TESOURA', 'PAPEL'))
