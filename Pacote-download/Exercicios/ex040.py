nota_1 = float(input('Digite su primeira nota: '))
nota_2 = float(input('Digite su segunda nota: '))
media = (nota_1 + nota_2)/2
if media < 5:
    print('Sua média é {:.2f}, voce foi \033[1;31m"REPROVADO"\033[m'.format(media))
elif media >= 5 and media < 6.9:
    print('Sua média é {:.2f}, você esta de \033[1;34m"RECUPERAÇÃO"\033[m'.format(media))
elif media > 7:
    print('\033[1;33mPARABENS!!!\033[m Sua média é de {:.2f}, e você foi \033[1;36m"APROVADO!!!\033[m'.format(media))
