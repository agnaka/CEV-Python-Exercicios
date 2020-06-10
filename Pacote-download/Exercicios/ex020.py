from random import shuffle
alu1 = input('Digite o nome do aluno 1: ')
alu2 = input('Digite o nme do aluno 2: ')
alu3 = input('Digite o nome do aluno 3: ')
alu4 = input('Digite o nome do aluno 4: ')
alunos = [alu1, alu2, alu3, alu4]

shuffle(alunos)
print('\033[1mA ordem de para a apresentação\033[m é \033[1;35m{}\033[m'.format(alunos))