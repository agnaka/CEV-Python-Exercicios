lista_1 = []
lista_par = []
lista_impar = []
while True:
    lista_1.append(int(input('Digite um número: ')))
    seguir = input('Quer continuar? [S/N] ').strip().upper()[0]
    while seguir not in 'SN':
        seguir = input('Quer continuar? [S/N] ').strip().upper()[0]
    if seguir == 'N':
        break
print('-=' * 25)
print(f'A lista comlpeta é {lista_1}')
for i in lista_1:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'A lista de pares é {lista_par}')
print(f'A lista de impares é {lista_impar}')
print('FIM')


