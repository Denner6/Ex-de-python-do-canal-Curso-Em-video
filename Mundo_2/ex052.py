import colorama
colorama.init()
tot = 0
n = int(input('Informe o número: ').strip())
mult = 0
for count in range(1, n+1):
    if n % count == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(count, end=' ')
print(f'\033[m\nO número {n} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele \033[32mÉ\033[m PRIMO!')
else:
    print('E por isso ele \033[31mNÃO\033[m É PRIMO!')


# Outro modo:

#n = int(input('Informe o número: ').strip())
#mult = 0
# for count in range(1, n+1):

#    if n % count == 0:
#       print(f'Múltiplo de {count}')
#       mult += 1

# if mult == 0:
#    print(f'O número {n} É PRIMO')
# else:
#    print(f'O número {n} NÃO é PRIMO')
