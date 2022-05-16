numeros_de_0_a_20 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                     'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))

    for cont in range(0, len(numeros_de_0_a_20)):
        if n == cont:
            print(f'Você digitou o número {numeros_de_0_a_20[cont]}')

        while n > 20 or n < 0:
            print('Tente novamente')
            n = int(input('Digite um número de 0 a 20: '))

    continuar = input('Você deseja continuar? [S/N] ').lower()
    if continuar == 'n':
        break
