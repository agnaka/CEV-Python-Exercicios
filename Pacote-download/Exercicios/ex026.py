frase = str(input('Digite cualquier frase: ')).upper().strip()
print('La letra \033[1;31m"A"\033[m aparece \033[31m{}\033[m veces en la frase'.format(frase.count('A')))
print('La primera letra \033[1;31m"A"\033[m aparece en la \033[7;33m{}\033[m posición'.format(frase.find('A')+1))
print('La última letra \033[1;31m"A"\033[m aparece en la \033[7;33m{}\033[m posición'.format(frase.rfind('A')+1))