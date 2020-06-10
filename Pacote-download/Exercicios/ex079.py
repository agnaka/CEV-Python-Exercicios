num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso ...')
    seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if seguir == 'N':
        break
num.sort()
print('-=' * 20)
print(f'Você digitou os valores {num}')
