print('=' * 40)
print(f'\033[1;36m{"EXERCÍCIO 105 - Função NOTAS":^40}\033[m')
print('=' * 40)

def notas(*num, sit=False):
    """
    -> Função apra analizar notas e situações de vários alunos.
    param num: uma oumias notas dos alunos (aceita várias).
    param sit: valor opcional, indicando se de deve adicionar ou não a situação. sit=False para não e sit+True para mostrar.
    return: dicionário com várias informações sobre a situação da turma.
    """
    lista = dict()
    lista['total'] = len(num)
    lista['maior'] = max(num)
    lista['menor'] = min(num)
    lista['média'] = sum(num)/len(num)
    if sit:
        if lista['média'] < 5:
            lista['situação'] = 'RUIM'
        if 7 > lista['média'] >= 5:
            lista['situação'] = 'RAZOÁVEL'
        if 7 < lista['média'] <= 10:
            lista['situação'] = 'BOA'
    return(lista)

# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, 2, sit=True)
print(resp)
help(notas)