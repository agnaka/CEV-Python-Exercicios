num = list()
num.append(int(input('Digite um valor: ')))
print('Adicionado ao final da lista ...')
for v in range(1,5):
    numero = int(input('Digite um valor: '))
    if numero >= max(num):
        num.append(numero)
        print('Adicionado ao final da lista ...')
    else:
        for p, i in enumerate(num): # sirve para comparar los valores del imput
            if numero < num[p]:
                num.insert(p, numero)
                print(f'Adicionado na posição {p} da lista...')
                break






'''            num.insert(p, numero)
            print(f'num[p] {num[p]}')
            print(f'Adicionado na posição {p+1} da lista...')
        else:
            num.append(numero)
            print('Adicionado ao final da lista ...')'''

print('-=' * 25)
print(f'OS valores digitados foram {num}')
