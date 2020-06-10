print('=' * 30)
print(f'\033[1;3;34m{"EXERCÍCIO 101 - FATORIAL":^30}\033[m')
print('=' * 30)

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    : param n: O número a ser calculado.
    : param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial do Fatorila de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end = '')
            if c > 1:
                print(f' x ', end = '')
            else:
                print('=', end = '')
    return f


# help(fatorial)
print(f' {fatorial(5, show=True)}')