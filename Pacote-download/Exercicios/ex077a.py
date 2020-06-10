palavra = ('Andres', 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis','estudiar', 'praticar' , 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = 'aeiouAEIOU'
for item in range(0,len(palavra)):
    print(f'\nNa palavra \033[1;33m{palavra[item].upper()}\033[m temos', end=' ')
    for letra in palavra[item]:
            if letra in vogais:
                print(f'\033[1;35m{letra.lower()}\033[m', end=' ')
print('\n')
print('-' * 30)
print('FIM')
