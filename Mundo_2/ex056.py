from time import sleep
idades = []
mais_velho = 0
menos_de_20 = []

homem_velho = ''
for i in range(1, 5):
    nome = input(
        f'Informe o NOME da {i}º pessoa: ').strip().title()
    print('------------------')
    sleep(0.5)
    sexo = input(f'Informe o GÊNERO da {i}º pessoa: ').strip().lower()
    print('------------------')
    sleep(0.5)
    idade = int(
        input(f'Informe a IDADE da {i}º pessoa: ').strip())
    print('------------------')
    sleep(0.5)

    idades.append(idade)
    if sexo == 'homem':
        if idade > mais_velho:
            mais_velho = idade
            homem_velho = nome.title()
    elif sexo == 'mulher':
        if idade < 21:
            menos_de_20 += 1


media = (idades[0] + idades[1] + idades[2] + idades[3]) / 4
#idades += idade
#media = idades / 4
print(f'A média das idades é {media}')
print(f' O homem mais velho é {homem_velho}')
print(f'{menos_de_20} mulheres tem menos de 21 anos.')
