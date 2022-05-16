from time import sleep

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('''
    [1]Sair
    [2]Não sair
    ''')
    opcao = int(input('Sua opção: '))
    for c in range(1, 16):
        print(f'{n} x  {c} = {n*c}')
    sleep(2)
    if opcao == 1:
        break
    else:
        continue
