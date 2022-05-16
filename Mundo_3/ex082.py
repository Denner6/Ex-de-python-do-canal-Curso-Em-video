lista_completa = []
pares = []
impares = []
while True:

    n = int(input('Digite um número: '))
    lista_completa.append(n)
    continuar = input('Quer continuar? [S/N] ').lower()

    while continuar != 'n' and continuar != 's':
        continuar = input('Quer continuar? [S/N] ')

    if continuar == 'n':
        break

for par in lista_completa:
    if par % 2 == 0:
        pares.append(par)

for impar in lista_completa:
    if impar % 2 == 1:
        impares.append(impar)
print(f'A lista completa é {", ".join(map(str,lista_completa))}')
print(f'A lista de pares é {", ".join(map(str,pares))}')
print(f'A lista de ímpares é {", ".join(map(str,impares))}')
