print('='* 30)
titulo = '\033[1;36mSEQUENCIA DE FIBONACCI\033[m'
print(f'{titulo:^40}')
print('=' * 30, '\n')
n = int(input('Digite quantos números da sequencia você quer ver: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=' -> ')
cont = 3
while cont<= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(t3, end=' -> ')
print('FIM')
print('_' * 30)