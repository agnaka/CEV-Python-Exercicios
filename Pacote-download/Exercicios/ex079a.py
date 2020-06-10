num = list()
while True:
    numero = (int(input('Digite um valor: ')))
    if numero in num:
        print('Valor duplicado! Não vou adicionar ...')
    else:
        num.append(numero)
        print('Valor adicionado com sucesso ...')
    seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if seguir == 'N':
        break
num.sort()
print('-=' * 20)
print(f'Você digitou os valores {num}')