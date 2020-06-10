num = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num <= 0:
        break
    for i in range (1,11):
        multi = i * num
        print(f'{num} x {i:2}= \033[1;36m{multi:2}\033[m')
    print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADO, Volte sempre!')