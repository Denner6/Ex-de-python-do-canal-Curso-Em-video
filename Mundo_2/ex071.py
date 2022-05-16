valor = int(input('Informe o valor a ser sacado: R$ '))
cinq, vint, dez, um = [0, 0, 0, 0]
while valor != 0:
    if valor >= 50:
        cinq = valor // 50
        valor -= cinq * 50
        print(f'Total de {cinq} notas de R$50.00')

    if valor >= 20:
        vint = valor // 20
        valor -= vint * 20
        print(f'Total de {vint} notas de R$20.00')

    if valor >= 10:
        dez = valor // 10
        valor -= dez * 10
        print(f'Total de {dez} notas de R$10.00')

    if valor >= 1:
        um = valor // 1
        valor -= um * 1
        print(f'Total de {um} notas de R$1.00')
