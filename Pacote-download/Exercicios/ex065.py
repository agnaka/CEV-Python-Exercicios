#n1 = int(input('Digite um número: '))
r = "S"
cont = maior = menor = som = 0
# maior = 0
# menor = 0
# soma = 0
while r == 'S':
    n1 = int(input('Digite um número: '))
    cont += 1
    r = str(input('Você quer continuar?  [S/N]')).upper().strip()[0]
    soma += n1
    media = soma / cont
    if cont == 1:
        menor = maior = n1
#       maior = n1
    else:
        if n1 < menor:
            menor = n1
        if n1 > maior:
            maior = n1
print(f'Você digitou {cont} números')
print(f'A soma é {soma}')
print(f'A média é {media:.2f}')
print( f'O número menor é \033[1;31m{menor}\033[m e o maior é \033[1;35m{maior}\033[m' )
print('FIM')
