print('_' * 55)
print('PROJEÇÃO ARITMÉTICA \033[1m"PA"033[m - 10 PRIMEIROS NÚEMROS')
print('_' * 55)
p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos números a mais você quer ver? \nDigite "0" para finalizar '))

print('FIM')