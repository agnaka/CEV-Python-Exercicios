sal = int(input('Qual é o seu salário atual?: '))
aumento = 0.15
sal_novo = sal + sal * aumento
print('Con aumento del \033[1;34m15%\033[m seu novo salário vai ser de \033[1;33mR${:.2f}\033[m'.format(sal_novo))