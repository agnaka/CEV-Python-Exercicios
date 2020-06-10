print('=' * 45)
print(f'LEITOR DE NÚMEROS EM EXTENSO'.center(45,' '))
print('=' * 45)
texto = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
compu = int(input('Digite um número entre 0 e 20: '))
while True:
    if compu < 0 or compu > 20:
        compu = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'\033[1mVocê digitou o número {texto[compu]}\033[m')
print('-' * 45)
print('FIM')