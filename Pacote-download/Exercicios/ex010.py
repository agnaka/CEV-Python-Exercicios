money = float(input('\033[4mQuanto dinheiro tem na sua carteira?:\033[m '))
dolar = 3.27
print('\033[1mVocê pode comprar\033[m \033[1;31m{:.2f}\033[m dólares'.format(money/dolar))