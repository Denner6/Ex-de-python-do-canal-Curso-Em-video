from random import randint


guardar_numeros = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10),)

print('Os valores sorteados foram: ', end=' ')
for n in guardar_numeros:
    print(n, end=' ')

maior = max(guardar_numeros)
menor = min(guardar_numeros)

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
