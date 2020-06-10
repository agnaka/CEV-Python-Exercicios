print('-=' * 20)
print('\033[1;34mCALCULADORA DEL ÍNDICE DE MASA MUSCULAR\033[m')
print('-=' * 20)
peso = float(input('Por favor digite seu peso: '))
altura = float(input('Por favor digite sua altura: '))
imc = peso / (altura ** 2)
# print(imc)
print('\033[1;4mTABELA DE IMC\033[m')
print('Abaixo de \033[1;36m18.5\033[m = Abaixo do Peso')
print('Entre \033[1;36m18.5\033[m e \033[1;36m25\033[m = Peso Ideal')
print('Entre \033[1;36m25\033[m e \033[1;36m30\033[m = Sobrepeso')
print('Entre \033[1;36m30\033[m e \033[1;36m40\033[m = Obesidade')
print('Acima de \033[1;36m40\033[m = Obesidade mórbida\n')
if imc < 18.5:
    print('Seu IMC é de {:.2f}.\n    Você esta \033[31mABAIXO DO PESO\033[m'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de {:.2f}.\n    \033[1;35mPARABENS!!!\033[m Você esta com o peso ideal'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é de {:.2f}.\n    \033[1;35mCUIDADO!!!\033[m \033[1;4mVocê esta com Sobrepesso\033[m'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.2f}.\n    \033[1;31mALERTA!!!\033[m \033[1;4mVocê esta \033[1;31mOBESO"\033[m'.format(imc))
else:
    print('Seu IMC é de {:.2f}.\n    \033[1;4;31mURGENTE VAI PROCURAR UM MÉDICO. VOCÊ ESTA COM OBESIDADE MÓRBIDA\033[m'.format(imc))