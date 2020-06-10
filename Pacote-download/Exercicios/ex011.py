lar = float(input('Qual é a largura da parede?: '))
alt = float(input('Qual a altura da parede?: '))
rend = 2
tinta = lar * alt / rend
print('La cantidad de tinta necessária para pintar a sua parede é de \033[1;34m{:.2f}\033[m litros'.format(tinta))