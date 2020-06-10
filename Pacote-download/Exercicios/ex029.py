vel = int(input('Escreve a sua velocidade: '))
if vel > 80:
    print('\033[1;4;31mVocê foi multado por excesso de velocidade\033[m')
    print('\033[1mLa multa vai custar\033[m \033[1;31mR$7,00\033[m \033[1mpor cada km acima do limite de\033[m \033[1;35m80km/h\033[m\nValor da multa = \033[1;4;7;33;44mR${}\033[m'.format((vel-80)*7))
else:
    print('\033[36mA sua velocidade esta dentro dos limites permitidos\033[m')