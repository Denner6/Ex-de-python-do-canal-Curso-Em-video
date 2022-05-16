def ajuda():
    from time import sleep
    cores = {'White': '\033[30m', 'Green': '\033[32m', 'Blue': '\033[34m', 'Red': '\033[31m', 'No color': '\033[m'}
    while True:
        print(f'{cores["Green"]}~' * 30)
        print('SISTEMA DE AJUDA Py HELP')
        print('~' * 30)
        funcao_ou_biblioteca = input(f'{cores["No color"]}Função ou biblioteca > ').lower()
        if funcao_ou_biblioteca != 'fim':
            print(f'{cores["Blue"]}~' * 40)
            print(f"Acessando manual do comando '{funcao_ou_biblioteca}'")
            print('~' * 40)
            sleep(2)
            print(f'{cores["White"]}')
            help(funcao_ou_biblioteca)
            print(f'{cores["No color"]}')
            sleep(1)
        if funcao_ou_biblioteca == 'fim':
            break
    print(f'{cores["Red"]}~'*30)
    print('FIM DO PROGRAMA!')
    print('~'*30)


ajuda()
