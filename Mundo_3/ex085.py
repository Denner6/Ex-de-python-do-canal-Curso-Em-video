numeros = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º número: '))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-='*30)
print(f'Os números ímpares são {", ".join(map(str,sorted(numeros[1])))}')
print(f'Os números pares são {", ".join(map(str,sorted(numeros[0])))}')
