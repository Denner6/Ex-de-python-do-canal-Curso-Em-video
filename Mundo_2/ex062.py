'''from time import sleep
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
msg = ''
opcao, cont = 1, 10

while opcao != 0:
    while cont >= 0:
        msg += f'{termo}'
        if cont != 0:
            msg += ' ➔  '
        termo += razao
        cont -= 1

    print(msg)
    opcao = int(input('Você deseja ver mais quantos termos? '))
    if opcao == 0:
        print('Saindo...')
        sleep(2)
        break
    else:
        opcao += 1
        while opcao != 1:
            msg += f' ➔  {termo}'
            termo += razao
            opcao -= 1
'''

# MODO GUANABARA (E MELHOR MODO)

print('Gerador de PA (Progreção Aritimedica)')
print('-='*20)
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ➔  ', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print(f'Progreção finalizada com {total} termos mostrados')
