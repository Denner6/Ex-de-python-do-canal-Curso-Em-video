temporaria = []
principal = []
maior = menor = 0
maior_nome = ''
menor_nome = ''
while True:
    temporaria.append(input('Nome: ').title())
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor= temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    continuar = input('Quer continuar? [S/N] ').lower()

    if continuar == 'n':
        break

for pessoa in principal:
    if pessoa[1] == maior:
        maior_nome += f'[{pessoa[0]}] '
    if pessoa[1] == menor:
        menor_nome += f'[{pessoa[0]}] '

print('-='*30)
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso é {maior}Kg. Peso de {maior_nome} ')
print(f'O menor peso foi de {menor}Kg. Peso de {menor_nome}')
