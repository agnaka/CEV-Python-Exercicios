def area(larg, comp):
    a = l * c
    print(f'A área de um terreno de {l}x{c} é de {a}m².')


print('Controle de Terrenos')
print('-' * 25)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
