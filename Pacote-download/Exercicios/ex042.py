r1 = int(input('Digite o primero segmento: '))
r2 = int(input('Digite o segundo segmento: '))
r3 = int(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os segmentos acima formam um TRIÁNGULO EQUILÁTERO')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print ('Os segmentos acima formam um TRIÁNGULO ISÓSCELES')
    else:
        print('Os segmentos acima formam um TRIÁNGULO ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÁNGULO')