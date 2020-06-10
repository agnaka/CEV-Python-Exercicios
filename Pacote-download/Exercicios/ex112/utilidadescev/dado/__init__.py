def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha:
            print(f'\033[1;31mERRO: \"{msg}\" é um preço inválido!\033[m)')
        else:
            valido = True
            return(float(entrada))
