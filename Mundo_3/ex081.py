numeros = []
numbers_typed = 0
position = 0

while True:

    n = int(input('Digite um número: '))
    numeros.append(n)
    numbers_typed += 1
    continuar = input('Quer continuar? [S/N] ').lower()

    while continuar != 'n' and continuar != 's':
        continuar = input('Quer continuar? [S/N] ').lower()
    if continuar == 'n':
        break


print('-='*30)
print(f'Você digitou {numbers_typed} números')
print(
    f"Os números em ordem decresente é {', '.join(map(str,sorted(numeros,reverse=True)))} ")
if 5 in numeros:
    position += 1
    print(f'O número 5 se encontra na posição {position+1}')

else:
    print('O número 5 não se encontra na lista')
