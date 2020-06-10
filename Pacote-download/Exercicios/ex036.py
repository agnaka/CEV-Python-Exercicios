casa = float(input('Qual o valor da casa que deseja? '))
sal = float(input('Qual o seu Salário? '))
anos = int(input('Em quantos anos pretende pagar o empréstimo? '))
parcela = casa / anos / 12
print('O valor da parcela fica em \033[1;32mR${:.2f}\033[m para uma casa do valor de \033[1;35mR${:.2f}\033[m e paga em \033[1;34m{}\033[m meses'.format(parcela, casa, int(anos * 12)))
if parcela > sal *.3:
    print('\033[1;31mINFELIZMENTE\033[m, Como a parcela representa mais do que \033[1;31m30%\033[m do seu salário, o empréstimo foi \033[4mnegado\033[m')
else:
    print('\033[1;4;36mPARABÉNS!!!\033[m Seu empréstimo foi aprovado, o valor mensal da parcela ficou em \033[1;4;33R${:.2f}\033[m por \033[4m{}\033[manos'.format(parcela, anos))