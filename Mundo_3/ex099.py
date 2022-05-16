from time import sleep


def maior(*valores):
    count = maior_numero = 0
    print('-='*30)
    print('Analizando os valores passados...')

    for number in valores:
        print(f'{number}', end=' ')
        sleep(0.1)
        if maior_numero <= valores[count]:
            maior_numero = valores[count]
            count += 1

    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi {maior_numero}')


# Main program
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 7, 0)
maior(1, 2)
maior()
