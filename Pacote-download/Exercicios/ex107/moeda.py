def metade(p):
    res = p / 2
    return(res)


def dobro(p):
    res = p * 2
    return(res)


def aumentar(p, a=0):
    res = p * (1 + (a/100))
    return(res)


def diminuir(p, a=0):
    res = p - (p * a / 100)
    return(res)
