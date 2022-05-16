soma = 0
cont = 0
for n in range(1,7):
    numero = int(input(f'Digite o {n}º número: '))
    if numero % 2 == 0:
        soma += numero
print(f'Você informou {n} números PARES e a soma entre eles é {soma}')
