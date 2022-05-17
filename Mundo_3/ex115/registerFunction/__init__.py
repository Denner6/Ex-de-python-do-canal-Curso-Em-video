from time import sleep

colors = {
    'Yellow': '\033[33m',
    'Blue': '\033[34m',
    'Red': '\033[31m',
    'Green': '\033[32m',
    'No color': '\033[m'
}


def menu():
    print('-' * 50)
    print('MAIN MENU'.center(50))
    print('-' * 50)
    print(f'{colors["Yellow"]}1 - {colors["Blue"]}View a register peoples {colors["No color"]}')
    print(f'{colors["Yellow"]}2 - {colors["Blue"]}Register a new people {colors["No color"]}')
    print(f'{colors["Yellow"]}3 - {colors["Blue"]}Left of the system {colors["No color"]}')
    print('-' * 50)


def register(arquivo='newRecords.txt', modo='a+'):
    with open(arquivo, modo) as file:  # , encoding='utf-8'

        while True:
            menu()
            option = input(f'{colors["Green"]}Your option: {colors["No color"]}').strip()

            while option != '1' and option != '2' and option != '3':
                print(f"{colors['Red']}ERROR: '{option}' not is a valid option! {colors['No color']}")
                sleep(1)
                menu()
                option = input(f'{colors["Green"]}Your option: {colors["No color"]}').strip()
                continue

            if option == '1':
                print('-' * 50)
                print('PEOPLES REGISTER'.center(50))
                print('-' * 50)
                file.seek(0)
                print(file.read())
                sleep(1)

            elif option == '2':
                print('-' * 50)
                print('NEW RECORD'.center(50))
                print('-' * 50)
                name = input('Nome: ').title()
                while True:
                    try:
                        years = int(input('Idade: '))
                    except:
                        print(f"{colors['Red']}ERROR, please type a valid number {colors['No color']} ")
                        continue
                    else:
                        file.write(f'{name:<42}{years} years\n')
                        print(f'Register of {name} added')
                        sleep(1)
                        break

            elif option == '3':
                print('-' * 50)
                print('Leaving of the system... See you later!'.center(50))
                print('-' * 50)
                break
