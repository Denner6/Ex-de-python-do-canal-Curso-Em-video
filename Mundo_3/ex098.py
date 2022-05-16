from time import sleep


def contagem(inicio, fim, passo):
    contador = inicio
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo += 1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if inicio > fim:
        while contador >= fim:
            print(contador, end=' ')
            contador -= passo
            sleep(0.5)
        print('FIM!')

    elif inicio < fim:
        while contador <= fim:
            print(contador, end=' ')
            contador += passo
            sleep(0.5)
        print('FIM!')


# Main program
contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
