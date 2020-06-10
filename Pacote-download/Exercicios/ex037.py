num = int(input('Digite un número inteiro: '))
conversao = int(input('Digite\n    \033[1;34m1\033[m para transformar em \033[1;33mbinário\033[m\n    \033[1;34m2\033[m para transformar em \033[1;33moctal\033[m\n    \033[1;34m3\033[m para transformar em \033[1;33mhexadecimal\033[m\n    '))
binario = bin(num)
octal= oct(num)
hexadecimal = hex(num)
if conversao == 1:
    print('O número decimal {} convertido em binário é {}'.format(num, binario [2:]))
elif conversao == 2:
    print('O número decimal {} convertido em octal é {}'.format(num, octal [2:]))
elif conversao == 3:
    print('O número decimal {} convertido em hexadecimal é {}'.format(num, hexadecimal[2:]))
else:
    print('Você digitou uma opção errada, por favor tente novamente')