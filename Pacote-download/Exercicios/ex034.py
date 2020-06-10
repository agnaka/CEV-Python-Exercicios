sal = float(input('Cuál es tu sueldo? '))
if sal > 1250:
    print('Si tu sueldo es de \033[32mR${:.2f}\033[m te corresponde un aumento del \033[1;35m10%\033[m, siendo el aumento de \033[1;35mR${:.2f}\033[m y tu nuevo sueldo de \033[1;4;34mR${:.2f}\033[m'.format(sal, (sal*0.10), (sal*1.1)))
else:
    print('Si tu sueldo es de R${:.2f} te corresponde un aumento del 15%, siendo el aumento de R${:.2f} y tu nuevo sueldo de R${:.2f}'.format(sal, (sal * 0.15), (sal * 1.15)))