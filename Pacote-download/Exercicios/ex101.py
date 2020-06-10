print('=' * 30)
print(f'\033[1;3;33m{"EXERCÍCIO 101 - VOTO":^30}\033[m')
print('=' *30)
def voto(a):
    from datetime import date
    atual = date.today().year
    idade = atual - a
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
