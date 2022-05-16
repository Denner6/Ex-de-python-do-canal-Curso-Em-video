print('Gerador de PA (Progreção Aritimedica)')
print('-='*20)
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
termo = a1
cont = 1
while cont <= 10:
    print(f'{termo} ➔  ', end='')
    termo += r
    cont += 1
print('FIM')
