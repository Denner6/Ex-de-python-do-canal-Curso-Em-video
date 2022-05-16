mais_pesado = 0
menos_pesado = 0
for i in range(1, 6):
    peso = float(input(f'Informe o peso da {i}º pessoa: '))
    if peso > mais_pesado:
        mais_pesado = peso
    else:
        menos_pesado = peso
print(f'Mais pesado {mais_pesado} kg')
print(f'Menos pesado {menos_pesado} kg')
