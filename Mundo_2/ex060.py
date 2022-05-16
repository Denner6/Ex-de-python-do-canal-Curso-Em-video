# Primeiro modo
'''n = int(input('Digite um número para ver seu fatorial: '))
fatorial = n

for i in range(1, fatorial):
    fatorial *= i
for j in range(n, 0, -1):
    print(j, end=' X ')
print(f'= {fatorial}')
print(f'O fatorial de {n} é {fatorial}')

'''
# segundo modo

'''from math import factorial


fatorial = int(input('Informe um número para ver seu fatorial: '))
count = fatorial
fatorialv2 = factorial(fatorial)
print(f'Fatorial de {fatorial}!')

while count > 0:
    count -= 1
    print(f'{fatorial} ✗ {count}', end='')

print(f'O fatorial de {fatorial} é {fatorialv2}')
'''

# Terceiro modo


from math import factorial
fatorial = int(input('Informe um número para ver seu fatorial: '))
count = fatorial
fatorialv2 = factorial(fatorial)
print(f'Calculando o fatorial de {fatorial}! = ', end='')

while count > 0:
    print(f'{count} ', end='')
    print('✗ ' if count > 1 else '= ', end='')
    count -= 1

print(fatorialv2)
print(f'O fatorial de {fatorial} é {fatorialv2}')
