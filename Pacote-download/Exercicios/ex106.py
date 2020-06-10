fun = ''
while True:
    print(f'\033[1;30;42m{"=" * 42}')
    print(f'{"  EXERCÍCIO 106 - SISTEMA DE AJUDA PyHELP"}')
    print(f'{"=" * 42}')
    fun = input('\033[m  Função ou Biblioteca > ').strip().lower()
    print(f'\033[1;30;44m{"-"}'* (len(fun) + 37))
    print(f"  Acessando o manual do comanado '{fun}'")
    print(f'{"-" * (len(fun) + 37)}')
    print('\033[0;30m', end = '')
    print('\033[7;30m', end = '')
    print(f'{help(fun)}')
    print('\033[m', end = '')
    if fun == "fim":
        print(f'\033[1;30;41m{"=" * 15}')
        print(f'{"  ATÉ LOGO!"}')
        print(f'{"=" * 15}')
        break

