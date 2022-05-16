import random
al1 = input('Aluno 1: ')
al2 = input('Aluno 2: ')
al3 = input('Aluno 3: ')
al4 = input('Aluno 4: ')
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print(' A ordem é:')
print(lista)