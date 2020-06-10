from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
if idade < 18:
    print('Você ainda vai se alistar em \033[1;34m{}\033[m anos'.format(18 - idade))
elif (2020-ano) > 18:
    print("Você passou do tempo de alistamento em \033[1;31m{}\033[m anos".format(idade - 18))
else:
    print('\033[1;4;32mÉ HORA DE SE ALISTAR!!!\033[m')