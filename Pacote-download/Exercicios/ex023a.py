num = int(input('Informe um número: '))
u = num //1 %10
d = num //10 %10
c = num //100 %10
d = num //1000 %10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('CEntrena: {}'.format(c))
print('Milhar: {}'.format(d))
