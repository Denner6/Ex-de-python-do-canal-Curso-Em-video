maior_18 = 0
homens = 0
mulheres = 0
while True:

    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo: [M/F] ').lower())

    while sexo != 'm' and sexo != 'f':
        sexo = str(input(f'Sexo: [M/F] ').lower())

    continuar = str(input('Quer continuar? [S/N] ').lower())

    while continuar != 's' and continuar != 'n':
        continuar = str(input('Quer continuar? [S/N] ').lower())

    if continuar == 'n':
        break

    if idade > 18:
        maior_18 += 1

    if idade < 20 and sexo == 'f':
        mulheres += 1

    if sexo == 'm':
        homens += 1


print('FIM DO PROGRAMA')
print('')
print(f'Foram resgistradas no total {maior_18} pessoas maiores de 18')
print(f'{mulheres} mulheres tem menos de 20 anos')
print(f'Foram registrados {homens} homens')
