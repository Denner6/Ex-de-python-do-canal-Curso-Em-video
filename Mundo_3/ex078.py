numeros = []
for i in range(0, 5):
    numeros.append(int(input(f'Digite o valor para a posição {i}: ')))

maior = max(numeros)
menor = min(numeros)

exibir = ''
posicao = 0
for j in numeros:
    if j == maior:
        exibir += f'{posicao}... '
    posicao += 1

posicao2 = 0
exibir2 = ''
for h in numeros:
    if h == menor:
        exibir2 += f'{posicao2}...'
    posicao2 += 1

print(f"Você digitou os valores", *numeros, sep=' ')
print(f'O menor valor digitado foi {menor} nas posições', exibir2)
print(f'O maior valor digitado foi {maior} nas posições', exibir)
