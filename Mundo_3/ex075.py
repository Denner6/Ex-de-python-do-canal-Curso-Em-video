n1 = int(input(f'Digite o 1º número: '))
n2 = int(input(f'Digite o 2º número: '))
n3 = int(input(f'Digite o 3º número: '))
n4 = int(input(f'Digite o 4º número: '))

numbers_typed = (n1, n2, n3, n4)
print(f'Você digitou os valores {numbers_typed}')
print(f'O valor 9 apareceu {numbers_typed.count(9)} vezes')

if 3 in numbers_typed:
    print(f'O valor 3 foi digitado na {numbers_typed.index(3)+1}ª posição')
else:
    print(f'O valor 3 foi digitado nenhuma vez')

print(f'O valores pares digitados foram ', end='')

while True:

    if n1 % 2 == 0:
        print(n1, end=' ')

    if n2 % 2 == 0:
        print(n2, end=' ')

    if n3 % 2 == 0:
        print(n3, end=' ')

    if n4 % 2 == 0:
        print(n4)

    else:
        print('nenhum')
    break
