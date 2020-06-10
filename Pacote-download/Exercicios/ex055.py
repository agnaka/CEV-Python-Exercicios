print('_' * 30)
print('\033[1;33mPESO DE 5 PESSOAS\033[m')
print('_' * 30)
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite el peso de la {}ª persona: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
''' if n > maior:
        maior = n
    if n < menor:
        menor = n
print('O maior peso é: {}'.format(maior))
print('O maior peso é: {}'.format(menor))'''
# print('{} e {}'.format(menor, maior))
