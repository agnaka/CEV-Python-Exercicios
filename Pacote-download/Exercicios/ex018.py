from math import radians, sin, cos, tan
ang = int(input('Digite um ângulo: '))
seno = sin(radians(ang))
cose = cos(radians(ang))
tang = tan(radians(ang))
print('Os valores do ángulo {}º digitado são:\n\033[1;31mseno {:.2f}\033[m\n\033[1;32mcoseno {:.2f}\033[m\n\033[1;33mhipotenusa {:.2f}\033[m'.format(ang, seno, cose, tang))
