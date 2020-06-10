def titulo(msg):
    print(f'\033[m-' * 40)
    print(f'{msg:}'.center(40))
    print(f'\033[m-' * 40)


def subtitulo(n, msg):
    print(f'\033[0;33m{n} \033[m- \033[0;34m{msg}\033[m')