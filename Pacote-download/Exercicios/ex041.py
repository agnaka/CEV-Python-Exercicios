from datetime import date
atual = date.today().year
ano = int(input('Qual é o ano de nascimento do atleta? '))
idade = int(atual - ano)
if idade <= 9:
    print('A sua categoria é \033[1;31mMIRIM\033[m')
elif idade > 9 and idade <= 14:
    print('A sua categoria é \033[1;32mINFANTIL\033[m')
elif idade > 14 and idade <= 19:
    print('A sua categoria é \033[1;33mJUNIOR\033[m')
elif idade > 19 and idade <= 20:
    print('A sua categoria é \033[1;34mSÊNIOR\033[m')
else:
    print('A sua categoria é \033[1;35mMASTER\033[m')