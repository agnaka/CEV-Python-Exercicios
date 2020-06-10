num = float(input('Digite una medida en metros: '))
print('La medida digitada es \033[1m{}\033[m y equivale a:\n\033[1;31m{}cm\033[m\n\033[1;36m{}mm\033[m'.format(num, num*10, num*100))