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


def diminuir(p=0, a=0, formato=False):
    res = p - (p * a / 100)
    return res if formato is False else moeda(res)
