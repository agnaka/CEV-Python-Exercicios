from time import sleep
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo e último número: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''Conforme a seguintes opções por favor digite a operação que gostaria de fazer : 
        \033[1;34m[1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS\033[m
        \033[1;31m[5] SAIR DO PROGRAMA\033[m

        A opção escolhida é: '''))
    if opcao == 1:
        soma = n1 + n2
        print('\033[1;32mA soma dos 2 números digitados é {}\033[m\n'.format(soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A multiplicação dos 2 númeroa digitados e {}'.format(multiplicar))
    elif opcao == 3:
        if n1 == n2:
            print('Os números são iguais')
        elif n1 > n2:
            print ('O primeiro número {} é maior que o segundo {}'.format(n1, n2))
        else:
            print('O segundo número {} é maior que o primeiro {}'.format(n2, n1))
    elif opcao == 4:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo e último número: '))
    print('=' * 50)
    sleep(2)


print('OBRIGADO')


''' elif opcao == 2:
        print('A multiplicação dos 2 númeroa digitados e {}'.format(multiplicar))
    elif opcao == 3:
        print('O número maior é {}'.format(n1))
    elif opcao == 4:
        print('no se')'''
