print(f'        \033[1;32mEXERCÍCIO 097\033[m')
print('=' * 30)

def escreva(txt):
    larg = len(txt) + 4
    print(f'-' * larg)
    print(f'{txt:^{larg}}')
    print(f'-' * larg)

while True:
    texto = str(input('Escreva um texto: '))
    escreva(texto)
    while True:
        seguir = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        if seguir in "SN":
            break
        print('Por favor digite "S" ou "N"')
    if seguir == "N":
        break
print('FIM!')
