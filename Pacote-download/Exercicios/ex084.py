cont =  maior = 0
pessoas = list()
dado = list()
dmax = list()
dmin = list()
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    cont +=1
    seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if seguir == 'N':
        break
min = pessoas[0][1]
for i, p in enumerate(pessoas):
    if (p[1]) < min:
        min = (p[1])
        pos = (i)
        dado.append(pessoas[pos][0])
        del dmin[:]
        dmin.append(dado[:])
        dado.clear()
    elif (p[1]) == min:
        min = (p[1])
        pos = (i)
        dado.append(pessoas[pos][0])
        dmin.append(dado[:])
        dado.clear()
for i, p in enumerate(pessoas):
    if (p[1]) > maior:
        maior = (p[1])
        pos = (i)
        dado.append(pessoas[pos][0])
        del dmax[:]
        dmax.append(dado[:])
        dado.clear()
    elif (p[1]) == maior:
        maior = (p[1])
        pos = (i)
        dado.append(pessoas[pos][0])
        dmax.append(dado[:])
        dado.clear()
# print(dmax)
# print(dmin)
print('-=' * 25)
print(f'O maior foi de {maior}kg. Peso de {dmax}')
print(f'O menor foi de {min}kg. Peso de {dmin}')
print(f'Ao todo você cadastrou {cont} pessoas.')
