lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    seguir = input('Quer continuar? [S/N] ').strip().upper()[0]
    while seguir not in 'SN':
        seguir = input('Quer continuar? [S/N] ').strip().upper()[0]
    if seguir == 'N':
        break
print('-=' * 25)
print(f'Você digitou \033[1;32m{cont}\033[m elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são \033[1;33m{lista}\033[m')
if 5 in lista:
    print('O valor \033[1;34m5\033[m faz parte da lista!')
else:
    print('O valor \033[1;35m5\033[m não foi encontrado na lista!')
print('FIM')