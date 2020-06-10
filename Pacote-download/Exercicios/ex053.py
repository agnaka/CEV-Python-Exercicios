print('=' * 60)
print('VAMOS A DESCOBRIR SE A FRASE QUE VOCÊ PENSOU É UM \033[1;35mPALÍNDROMO\033[m')
print('=' * 60)
f = input('Digite una frase: ')
fr = f.upper()
frase = fr.replace(' ', '')
print(frase)
inverso = frase[::-1]
'''l = int(len(frase))
print(l)
inverso = ''
for letra in range(l-1, -1, -1):
    inverso += frase[letra]'''

if inverso != frase:
    print('A frase "{}" não é um palíndromo'.format(f))
else:
    print('PALÍNDROMO')