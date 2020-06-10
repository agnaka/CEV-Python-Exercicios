price = float(input('\033[4mQual é a distância da sua viagem:\033[m '))
if price<= 200:
    print('\033[1mO preço da passagem é de\033[m \033[1;33mR${:.2f}\033[m'.format(price * 0.5))
else:
    print('\033[1mO preço da sua passagem é de\033[m \033[1;37mR${:.2f}\033[m'.format(price * 0.45))