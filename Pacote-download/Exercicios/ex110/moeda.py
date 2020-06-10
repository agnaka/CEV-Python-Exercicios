def moeda(p=0, moeda = 'R$'):
    return f'{moeda}{p:>2.2f}'.replace('.', ',')


def metade(p = 0, formato=False):
    res = p / 2
    return res if formato is False else moeda(res)


def dobro(p = 0, formato=False):
    res = p * 2
    return res if not formato else moeda(res)


def aumentar(p= 0, a=0, formato=False):
    res = p * (1 + (a/100))
    return res if not formato else moeda(res)


def diminuir(p=0, r=0, formato=False):
    res = p * (1 - (r / 100))
    return res if formato is False else moeda(res)


def resumo(p=0, a=10, r=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço:  \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a, True)}')
    print(f'{r}% de redução: \t{diminuir(p, r, True)}')
    print('-' * 30)
