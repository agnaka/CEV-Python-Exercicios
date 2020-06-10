def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO! \"{entrada}\" é um preço inválido\033[m')
        else:
            valido = True
            return float(entrada)


def leaint(n):
    if n.isnumeric():
        n = int(n)
    else:
        print('\033[31mERRO! Digite um número inteiro válido\033[m')
        n = leaint(input('Digite um número: '))
    return (n)